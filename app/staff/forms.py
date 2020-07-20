from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, FloatField, IntegerField, TextAreaField
from flask_wtf.file import FileField, FileRequired, FileAllowed
from wtforms.validators import ValidationError, DataRequired, Email, EqualTo

class AddItem(FlaskForm):
    item_title = StringField('Item Name', validators=[DataRequired()])
    quantity = IntegerField('Item Quantity', validators=[DataRequired()])
    price = FloatField('Item Price')
    warranty = IntegerField('Item Warranty', validators=[DataRequired()])
    slider_image = FileField(validators=[FileRequired(), FileAllowed(['jpg', 'png'], 'Images only!')])
    single_image = FileField(validators=[FileRequired(), FileAllowed(['jpg', 'png'], 'Images only!')])
    key_features = TextAreaField()
    key_benefits = TextAreaField(validators=[DataRequired()])
    advert_text = TextAreaField(validators=[DataRequired()])
    post_installation = TextAreaField(validators=[DataRequired()])
    delivery_lagos = TextAreaField(validators=[DataRequired()])
    delivery_outside_express = TextAreaField(validators=[DataRequired()])
    delivery_outside_normal = TextAreaField(validators=[DataRequired()])
    submit = SubmitField('Add item')
    
