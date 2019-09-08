import os


def export_vars(request):
    data = {}
    data['WORKGEN_MODE'] = os.environ.get('WORKGEN_MODE', 'prod')
    return data
