import pynvml

class GPUStats:
    """Get statistics for a specific GPU device, e.g. current memory usage."""

    def __init__(self, device: int = 0):
        """Get information on a specific GPU device

        Parameters
        ----------
        device : int
            Number of the GPU device you want to measure
        """
        self.device = device

    def info(self):
        pynvml.nvmlInit()
        handle = pynvml.nvmlDeviceGetHandleByIndex(self.device)
        info = pynvml.nvmlDeviceGetMemoryInfo(handle)
        return info

    def total(self):
        """Get MB of total memory (free + used) on GPU."""
        return self.info().total/1024**2

    def free(self):
        """Get MB of free memory on GPU."""
        # Returns in MB
        return self.info().free/1024**2

    def used(self):
        """Get MB of used memory on GPU."""
        return self.info().used/1024**2

    def print(self):
        """Print info on current GPU utilization."""
        info = self.info()
        print(f"GPU memory usage: {info.used//1024**2} / {info.total//1024**2} MB")

class ModelStats:
    """Get statistics for a specific PyTorch model, e.g. total number of parameters."""
    
    def __init__(self, model):
        """Get information on a specific PyTorch model.

        Parameters
        ----------
        model : nn.Module
            PyTorch model
        """
        self.model = model
        # Cache values
        self._total = None
        self._trainable = None
        self._frozen = None

    def total(self) -> int:
        """Get total number of parameters in model."""
        if self._total is None:
            self._total = sum(
                param.numel() for param in self.model.parameters()
            )
        return self._total
        
    def trainable(self) -> int:
        """Get number of trainable parameters in model."""
        if self._trainable is None:
            self._trainable = sum(
                p.numel() for p in self.model.parameters() if p.requires_grad
            )
        return self._trainable
        
    def frozen(self) -> int:
        """Get number of non-trainable parameters in model."""
        if self._frozen is None:
            self._frozen = self.total() - self.trainable()
        return self._frozen
        
    def print(self):
        """Print info on number of parameters in model."""
        print(f"{self.total()} params ({self.trainable()} trainable | {self.frozen()} non-trainable)")
