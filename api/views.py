from rest_framework.generics import ListAPIView,RetrieveAPIView,RetrieveUpdateAPIView,DestroyAPIView,CreateAPIView
from restaurants.models import Restaurant
from .serializers import RestaurantListSerializer,RestaurantDetailSerializer,RestaurantUpdateSerializer

class RestaurantListView(ListAPIView):
	queryset = Restaurant.objects.all()
	serializer_class = RestaurantListSerializer

class RestaurantDetailView(RetrieveAPIView):
	queryset = Restaurant.objects.all()
	serializer_class = RestaurantDetailSerializer
	lookup_field = 'id'
	lookup_url_kwarg = 'restaurant_id'


class RestaurantUpdateView(RetrieveUpdateAPIView):
	queryset = Restaurant.objects.all()
	serializer_class = RestaurantUpdateSerializer
	lookup_field = 'id'
	lookup_url_kwarg = 'restaurant_id'

class RestaurantDeleteView(DestroyAPIView):
	queryset = Restaurant.objects.all()
	lookup_field = 'id'
	lookup_url_kwarg = 'restaurant_id'

class RestaurantCreateView(CreateAPIView):
    serializer_class = RestaurantUpdateSerializer


    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)