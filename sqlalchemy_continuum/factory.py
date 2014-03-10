class ModelFactory(object):
    model_name = None

    def __init__(self, manager):
        self.manager = manager

    def __call__(self):
        """
        Create model class but only if it doesn't already exist
        in declarative model registry.
        """
        registry = self.manager.declarative_base._decl_class_registry
        if self.model_name not in registry:
            return self.create_class()
        return registry[self.model_name]