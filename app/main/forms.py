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
    # pitch = TextAreaField('Your Pitch', validators=[Required()])
    category = SelectField('Category', choices=[('Interview', 'Interview'), ('Academic', 'Academic'), ('Music', 'Music'),('Technology','Technology'),('Health','Health')],validators=[Required()])
    content = TextAreaField('YOUR PITCH',validators=[Required()])
    submit = SubmitField('Create')

class CommentForm(FlaskForm):
        Comment = TextAreaField('Comment', validators=[Required()])
    submit = SubmitField('Post Comment')