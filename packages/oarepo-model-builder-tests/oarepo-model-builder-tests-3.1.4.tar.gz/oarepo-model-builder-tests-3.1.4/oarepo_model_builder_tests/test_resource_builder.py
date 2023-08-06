from oarepo_model_builder.invenio.invenio_base import InvenioBaseClassPythonBuilder


class TestResourceBuilder(InvenioBaseClassPythonBuilder):
    TYPE = "invenio_tests_resource"
    template = "test_resource"
    MODULE = "tests.test_resource"

    def finish(self, **extra_kwargs):
        python_path = self.module_to_path(self.MODULE)
        self.process_template(
            python_path,
            self.template,
            schema=self.schema,
            **extra_kwargs,
        )