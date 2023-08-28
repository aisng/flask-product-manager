from flask_wtf import FlaskForm
from wtforms.fields import (
    StringField,
    IntegerField,
    FloatField,
    SubmitField,
    TextAreaField,
    SelectField,
)
from wtforms.validators import DataRequired, Length


class ProductForm(FlaskForm):
    name = StringField(
        "Product name", validators=[DataRequired(message="Required field.")]
    )
    description = TextAreaField(
        "Description",
        validators=[
            DataRequired(message="Required field."),
            Length(max=70, message="Maximum 70 symbols."),
        ],
    )
    price = FloatField("Price", validators=[DataRequired(message="Required field.")])
    quantity = IntegerField(
        "Quantity", validators=[DataRequired(message="Required field.")]
    )
    submit = SubmitField("Submit")


class SelectProductForm(FlaskForm):
    product = SelectField(
        "Products", validators=[DataRequired(message="Must select a product.")]
    )
    submit = SubmitField("Select")
