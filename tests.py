from wtforms import Form, fields
from wtforms_test import FormTestCase


class ExampleForm(Form):
    textarea = fields.TextAreaField()
    text = fields.TextField()
    integer = fields.IntegerField()
    datetime = fields.DateTimeField()
    select = fields.SelectField(choices=[(i, i) for i in xrange(3)])


class TestFormTestCase(FormTestCase):
    form_class = ExampleForm

    def test_assert_type(self):
        self.assert_type('text', fields.TextField)
        self.assert_type('textarea', fields.TextAreaField)
        self.assert_type('integer', fields.IntegerField)

    def test_assert_choices(self):
        self.assert_choices('select', [(i, i) for i in xrange(3)])

    def test_assert_choice_values(self):
        self.assert_choice_values('select', [(2, 2), (0, 0), (1, 1)])
