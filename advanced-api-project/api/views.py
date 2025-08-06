from rest_framework import generics, filters
from django_filters.rest_framework import DjangoFilterBackend, FilterSet, CharFilter, NumberFilter
from .models import Book
from .serializers import BookSerializer
from rest_framework.permissions import IsAuthenticatedOrReadOnly

# Custom FilterSet to enforce exact match
class BookFilter(FilterSet):
    title = CharFilter(field_name='title', lookup_expr='exact')
    author_name = CharFilter(field_name='author__name', lookup_expr='exact')
    publication_year = NumberFilter(field_name='publication_year', lookup_expr='exact')

    class Meta:
        model = Book
        fields = ['title', 'author_name', 'publication_year']

# Views
class BookListView(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_class = BookFilter
    search_fields = ['title', 'author__name']
    ordering_fields = ['title', 'publication_year']
    permission_classes = [IsAuthenticatedOrReadOnly]

class BookCreateView(generics.CreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

class BookDetailView(generics.RetrieveAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

class BookUpdateView(generics.UpdateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

class BookDeleteView(generics.DestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
