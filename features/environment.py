from django.test.runner import DiscoverRunner

def before_scenario(context, scenario):
    context.runner = DiscoverRunner()
    context.runner.setup_test_environment()
    context.client = None

def after_scenario(context, scenario):
    context.runner.teardown_test_environment()
