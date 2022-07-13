from django.shortcuts import render

# Create your views here.
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import authentication, permissions
from django.contrib.auth.models import User
from .serializers import RegistrationSerializer,UserLoginSerializer,\
                         BookSerializer, MemberSerializer,BookViewSerializer
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import authentication, permissions
from django.contrib.auth.models import User
from .models import Book
class UserRegistrationView(APIView):
    serializer_class = RegistrationSerializer
    permission_classes = (permissions.AllowAny, )

    def post(self, request):
        print(request.data)
        serializer = self.serializer_class(data=request.data)
        valid = serializer.is_valid(raise_exception=True)

        if valid:
            serializer.save()
            status_code = status.HTTP_201_CREATED

            response = {
                'success': True,
                'statusCode': status_code,
                'message': 'User successfully registered!',
                'user': serializer.data
            }

            return Response(response, status=status_code)



class UserLoginView(APIView):
    serializer_class = UserLoginSerializer
    permission_classes = (permissions.AllowAny, )

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        valid = serializer.is_valid(raise_exception=True)

        if valid:
            status_code = status.HTTP_200_OK

            response = {
                'success': True,
                'statusCode': status_code,
                'message': 'User logged in successfully',
                'access': serializer.data['access'],
                'refresh': serializer.data['refresh'],
                'authenticatedUser': {
                    'email': serializer.data['email'],
                    'role': serializer.data['role']
                }
            }

            return Response(response, status=status_code)



class BookCreateView(APIView):
    serializer_class = BookSerializer
    permission_classes = (permissions.IsAuthenticated,)

    def post(self, request):
        user = User.objects.get(username=request.user.username)
        list2 = [] 
        for i in user.groups.all():
            list2.append(i.name)
        if 'Librarian' not  in list2:
            response = {
                'success': False,
                'status_code': status.HTTP_403_FORBIDDEN,
                'message': 'You are not authorized to perform this action'
            }
            return Response(response, status.HTTP_403_FORBIDDEN)
        else:
            serializer = self.serializer_class(data=request.data)
            valid = serializer.is_valid(raise_exception=True)

            if valid:
                serializer.save()
                status_code = status.HTTP_201_CREATED

                response = {
                    'success': True,
                    'statusCode': status_code,
                    'message': 'Book created successfully!',
                    'user': serializer.data
                }

                return Response(response, status=status_code)


class BookView(APIView):
    serializer_class = BookSerializer
    permission_classes = (permissions.IsAuthenticated,)

    def get(self, request,id):
        user = User.objects.get(username=request.user.username)
        try:
            book = Book.objects.get(id=id)
        except Book.DoesNotExist:
            response = {
                'success': False,
                'status_code': status.HTTP_404_NOT_FOUND,
                'message': 'Book does not exist.'
            }
            return Response(response, status.HTTP_404_NOT_FOUND)
        list2 = [] 
        for i in user.groups.all():
            list2.append(i.name)
        if 'Librarian' not  in list2:
            response = {
                'success': False,
                'status_code': status.HTTP_403_FORBIDDEN,
                'message': 'You are not authorized to perform this action'
            }
            return Response(response, status.HTTP_403_FORBIDDEN)
        else:
            serializer = self.serializer_class(book)
            
            status_code = status.HTTP_200_OK

            response = {
                    'success': True,
                    'statusCode': status_code,
                    'user': serializer.data
                }

            return Response(response, status=status_code)
       
    def put(self, request,id):
        user = User.objects.get(username=request.user.username)
        try:
            book = Book.objects.get(id=id)
        except Book.DoesNotExist:
            response = {
                'success': False,
                'status_code': status.HTTP_404_NOT_FOUND,
                'message': 'Book does not exist.'
            }
            return Response(response, status.HTTP_404_NOT_FOUND)
        list2 = [] 
        for i in user.groups.all():
            list2.append(i.name)
        if 'Librarian' not  in list2:
            response = {
                'success': False,
                'status_code': status.HTTP_403_FORBIDDEN,
                'message': 'You are not authorized to perform this action'
            }
            return Response(response, status.HTTP_403_FORBIDDEN)
        else:
            serializer = self.serializer_class(book,request.data)
            valid = serializer.is_valid(raise_exception=True)

            if valid:
                serializer.save()
                status_code = status.HTTP_200_OK

                response = {
                    'success': True,
                    'statusCode': status_code,
                    'message': "Book updated successfully!",
                    'user': serializer.data
                }

                return Response(response, status=status_code)
       
    def delete(self, request,id):
        user = User.objects.get(username=request.user.username)
        try:
            book = Book.objects.get(id=id)
        except Book.DoesNotExist:
            response = {
                'success': False,
                'status_code': status.HTTP_404_NOT_FOUND,
                'message': 'Book does not exist.'
            }
            return Response(response, status.HTTP_404_NOT_FOUND)
        list2 = [] 
        for i in user.groups.all():
            list2.append(i.name)
        if 'Librarian' not  in list2:
            response = {
                'success': False,
                'status_code': status.HTTP_403_FORBIDDEN,
                'message': 'You are not authorized to perform this action'
            }
            return Response(response, status.HTTP_403_FORBIDDEN)
        else:
            book.delete() 
        
            
            status_code = status.HTTP_200_OK

            response = {
                    'success': True,
                    'statusCode': status_code,
                    'message': "Book deleted successfully",
                    
            }

            return Response(response, status=status_code)
       
    

class MemberCreateView(APIView):
    serializer_class = MemberSerializer
    permission_classes = (permissions.IsAuthenticated,)

    def post(self, request):
        user = User.objects.get(username=request.user.username)
        list2 = [] 
        for i in user.groups.all():
            list2.append(i.name)
        if 'Librarian' not  in list2:
            response = {
                'success': False,
                'status_code': status.HTTP_403_FORBIDDEN,
                'message': 'You are not authorized to perform this action'
            }
            return Response(response, status.HTTP_403_FORBIDDEN)
        else:
            serializer = self.serializer_class(data=request.data)
            valid = serializer.is_valid(raise_exception=True)

            if valid:
                serializer.save()
                status_code = status.HTTP_201_CREATED

                response = {
                    'success': True,
                    'statusCode': status_code,
                    'message': 'Member created Successfully',
                    'user': serializer.data
                }

                return Response(response, status=status_code)


class MemberView(APIView):
    serializer_class = MemberSerializer
    permission_classes = (permissions.IsAuthenticated,)

    def get(self, request,id):
        user = User.objects.get(username=request.user.username)
        try:
            member = User.objects.get(id=id)
        except User.DoesNotExist:
            response = {
                'success': False,
                'status_code': status.HTTP_404_NOT_FOUND,
                'message': 'Member does not exist.'
            }
            return Response(response, status.HTTP_404_NOT_FOUND)
        list2 = [] 
        for i in user.groups.all():
            list2.append(i.name)
        if 'Librarian' not  in list2:
            response = {
                'success': False,
                'status_code': status.HTTP_403_FORBIDDEN,
                'message': 'You are not authorized to perform this action'
            }
            return Response(response, status.HTTP_403_FORBIDDEN)
        else:
            serializer = self.serializer_class(member)
            
            status_code = status.HTTP_200_OK

            response = {
                    'success': True,
                    'statusCode': status_code,
                    'user': serializer.data
                }

            return Response(response, status=status_code)
       
    def put(self, request,id):
        user = User.objects.get(username=request.user.username)
        try:
            member = User.objects.get(id=id)
        except User.DoesNotExist:
            response = {
                'success': False,
                'status_code': status.HTTP_404_NOT_FOUND,
                'message': 'Member does not exist.'
            }
            return Response(response, status.HTTP_404_NOT_FOUND)
        list2 = [] 
        for i in user.groups.all():
            list2.append(i.name)
        if 'Librarian' not  in list2:
            response = {
                'success': False,
                'status_code': status.HTTP_403_FORBIDDEN,
                'message': 'You are not authorized to perform this action'
            }
            return Response(response, status.HTTP_403_FORBIDDEN)
        else:
            serializer = self.serializer_class(member,request.data)
            valid = serializer.is_valid(raise_exception=True)

            if valid:
                serializer.save()
                status_code = status.HTTP_200_OK

                response = {
                    'success': True,
                    'statusCode': status_code,
                    'message': "Member updated successfully",
                    'user': serializer.data
                }

                return Response(response, status=status_code)
       
    def delete(self, request,id):
        user = User.objects.get(username=request.user.username)
        try:
            member = User.objects.get(id=id)
        except User.DoesNotExist:
            response = {
                'success': False,
                'status_code': status.HTTP_404_NOT_FOUND,
                'message': 'Member does not exist.'
            }
            return Response(response, status.HTTP_404_NOT_FOUND)
        list2 = [] 
        for i in user.groups.all():
            list2.append(i.name)
        if 'Librarian' not  in list2:
            response = {
                'success': False,
                'status_code': status.HTTP_403_FORBIDDEN,
                'message': 'You are not authorized to perform this action'
            }
            return Response(response, status.HTTP_403_FORBIDDEN)
        else:
            member.delete() 
        
            
            status_code = status.HTTP_200_OK

            response = {
                    'success': True,
                    'statusCode': status_code,
                    'message': "Member deleted successfully",
                    
            }

            return Response(response, status=status_code)
       
         

class MemberBookView(APIView):
    serializer_class = BookViewSerializer
    permission_classes = (permissions.IsAuthenticated,)

    def get(self, request):
        user = User.objects.get(username=request.user.username)
        
        list2 = [] 
        for i in user.groups.all():
            list2.append(i.name)
        if 'Member' not  in list2:
            response = {
                'success': False,
                'status_code': status.HTTP_403_FORBIDDEN,
                'message': 'You are not authorized to perform this action'
            }
            return Response(response, status.HTTP_403_FORBIDDEN)
        else:
            member = Book.objects.filter(status="Available")
            print(member)
            serializer = self.serializer_class(member,many=True)
            
            status_code = status.HTTP_200_OK

            response = {
                    'success': True,
                    'statusCode': status_code,
                    'message': "List of avaiable books",
                    'user': serializer.data
                }

            return Response(response, status=status_code)


class MemberBookBorrowView(APIView):
    serializer_class = BookSerializer
    permission_classes = (permissions.IsAuthenticated,)

    def get(self, request,id):
        user = User.objects.get(username=request.user.username)
        try:
            member = Book.objects.get(id=id)
        except Book.DoesNotExist:
            response = {
                'success': False,
                'status_code': status.HTTP_404_NOT_FOUND,
                'message': 'Book does not exist.'
            }
            return Response(response, status.HTTP_404_NOT_FOUND)
        list2 = [] 
        for i in user.groups.all():
            list2.append(i.name)
        if 'Member' not  in list2:
            response = {
                'success': False,
                'status_code': status.HTTP_403_FORBIDDEN,
                'message': 'You are not authorized to perform this action'
            }
            return Response(response, status.HTTP_403_FORBIDDEN)
        else:
            member.status = "Borrowed"
            member.save()
            status_code = status.HTTP_200_OK

            response = {
                    'success': True,
                    'statusCode': status_code,
                    'message': "Book Borrowed Successfully",
                
                }

            return Response(response, status=status_code)
       
    
class MemberBookReturnView(APIView):
    serializer_class = BookSerializer
    permission_classes = (permissions.IsAuthenticated,)

    def get(self, request,id):
        user = User.objects.get(username=request.user.username)
        try:
            member = Book.objects.get(id=id)
        except Book.DoesNotExist:
            response = {
                'success': False,
                'status_code': status.HTTP_404_NOT_FOUND,
                'message': 'Book does not exist.'
            }
            return Response(response, status.HTTP_404_NOT_FOUND)
        list2 = [] 
        for i in user.groups.all():
            list2.append(i.name)
        if 'Member' not  in list2:
            response = {
                'success': False,
                'status_code': status.HTTP_403_FORBIDDEN,
                'message': 'You are not authorized to perform this action'
            }
            return Response(response, status.HTTP_403_FORBIDDEN)
        else:
            member.status = "Available"
            member.save()
            status_code = status.HTTP_200_OK

            response = {
                    'success': True,
                    'statusCode': status_code,
                    'message': "Book Returned successfully",
                    
                }

            return Response(response, status=status_code)
       
        
    
class MemberDeleteAccountView(APIView):
    serializer_class = BookSerializer
    permission_classes = (permissions.IsAuthenticated,)

    def delete(self, request):
        user = User.objects.get(username=request.user.username)
        try:
            member = User.objects.get(username=request.user.username)
        except User.DoesNotExist:
            response = {
                'success': False,
                'status_code': status.HTTP_404_NOT_FOUND,
                'message': 'User does not exist.'
            }
            return Response(response, status.HTTP_404_NOT_FOUND)
        list2 = [] 
        for i in user.groups.all():
            list2.append(i.name)
        if 'Member' not  in list2:
            response = {
                'success': False,
                'status_code': status.HTTP_403_FORBIDDEN,
                'message': 'You are not authorized to perform this action'
            }
            return Response(response, status.HTTP_403_FORBIDDEN)
        else:
            member.delete()
            status_code = status.HTTP_200_OK

            response = {
                    'success': True,
                    'statusCode': status_code,
                    'message': "Member Account deleted successfully",
                
                }

            return Response(response, status=status_code)
       
                  