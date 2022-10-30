from .models import SubscriberEmail,Category

def createUserSubscription(name,email):
    users = SubscriberEmail.objects.filter(name=name,email=email)
    if not users.exists():
        SubscriberEmail.objects.create(name=name,email=email)
        return 1
    return 0


def getAllCategories():
    category = Category.objects.all()
    return category
