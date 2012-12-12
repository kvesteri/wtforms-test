WTForms-Test
============

WTForms-Test provides various pytest unittest helpers for testing WTForms based forms.

QuickStart
----------

Consider the following simple form.

::

    from wtforms import Form
    from wtforms.fields import IntegerField
    from wtforms.validators import DataRequired


    class UserForm(Form):
        age = IntegerField(validators=[DataRequired()])


Writing tests for would be as easy as: ::

    from wtforms_test import FormTestCase


    class TestUserForm(FormTestCase):
        form_class = UserForm

        def test_age_is_required(self):
            self.assert_required('age')


Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`

