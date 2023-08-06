################################################################################
import functools
def register():
    def wrapped(fn):
        @functools.wraps(fn)
        def wrapped_f(*args, **kwargs):
            return fn(*args, **kwargs)
        wrapped_f.methodName = wrapped_f.__name__ 
        wrapped_f.methodDescription = wrapped_f.__doc__ 
        return wrapped_f
    return wrapped

@register()
def OutputMethodMetadata(method):
    '''Outputs the stored metadata for the given method object'''
    print(method.methodName)
    print(method.methodDescription)
################################################################################