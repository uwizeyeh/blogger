from flask_wtf import FlaskForm
from wtforms import StringField,TextAreaField,SubmitField
from wtforms.validators import Required

class ReviewForm(FlaskForm):

    title = StringField('Review title',validators=[Required()])
    review = TextAreaField('Movie review', validators=[Required()])
    submit = SubmitField('Submit')
    
class UpdateProfile(FlaskForm):
    bio = TextAreaField('Tell us about you.',validators = [Required()])
    submit = SubmitField('Submit')
# class LoginForm(FlaskForm):
#     email = StringField('Your Email Address',validators=[Required(),Email()])
#     password = PasswordField('Password',validators =[Required()])
#     remember = BooleanField('Remember me')
#     submit = SubmitField('Sign In')

class PitchForm(FlaskForm):
    pitch = TextAreaField('Your Pitch', validators=[Required()])
    # category_id = SelectField('Select Category', choices=[('1', 'Interview'), ('2', 'Pick Up Lines'), ('3', 'Promotion'),('4','Product')])
    # content = TextAreaField('YOUR PITCH')
    submit = SubmitField('Create')

# class UpvoteForm(FlaskForm):
#     '''
#     Class to create a wtf form for upvoting a pitch
#     '''
#     submit = SubmitField('Upvote')