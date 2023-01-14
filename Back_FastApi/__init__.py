from db_src.db_models import user_models, orders_model, product_models
from db_src import database


def create_database():
    user_models.UserModel()
    orders_model.OrderModel()
    orders_model.CartModel()
    orders_model.PaymentHistoryModel()
    product_models.ProductModel()
    product_models.DiscountModel()
    return database.Base.metadata.create_all(bind=database.engine)


# create_database()
