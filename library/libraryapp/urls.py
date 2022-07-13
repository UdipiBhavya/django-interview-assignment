from django.urls import path


from .views import (
    UserRegistrationView,
    UserLoginView,
    BookCreateView,
    BookView,
    MemberCreateView,
    MemberView,
    MemberBookView,
    MemberBookBorrowView,
    MemberBookReturnView,
    MemberDeleteAccountView
  
)

urlpatterns = [
   
    path('register', UserRegistrationView.as_view(), name='register'),
    path('login', UserLoginView.as_view(), name='login'),
    path('create/books',BookCreateView.as_view(),name="book_create_view"),
    path('book/<int:id>',BookView.as_view(),name="book_view"),
    path('create/members',MemberCreateView.as_view(),name="member_create_view"),
    path('member/<int:id>',MemberView.as_view(),name="member_view"),
    path('view/all/available/books',MemberBookView.as_view(),name="member_book_view"),
    path('borrow/book/<int:id>',MemberBookBorrowView.as_view(),name="member_book_borrorw_view"),
    path('return/book/<int:id>',MemberBookReturnView.as_view(),name="member_book_return_view"),
    path('delete/member',MemberDeleteAccountView.as_view(),name="delete_account_view")
   
   
   
]