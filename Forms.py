from wtforms import Form, StringField, RadioField, SelectField, TextAreaField, validators, BooleanField

class CreateUserForm(Form):
    firstName = StringField('First Name', [validators.Length(min=1,
                max=150), validators.DataRequired()])
    lastName = StringField('Last Name', [validators.Length(min=1,
                max=150), validators.DataRequired()])
    membership = RadioField('Membership', choices=[('F', 'Fellow'),
                ('S', 'Senior'), ('P', 'Professional')], default='F')
    gender = SelectField('Gender', [validators.DataRequired()],
                choices=[('', 'Select'), ('F', 'Female'), ('M', 'Male')], default='')
    remarks = TextAreaField('Remarks', [validators.Optional()])
    product1 = BooleanField('Product1')
