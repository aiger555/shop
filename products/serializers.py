from rest_framework import serializers

from .models import (
    Advantages,
    Category,
    Collection,
    FloatingButton, 
    Product, 
    ProductColor, 
    ProductImage,
    Favorite,
    AboutUs,
    AboutUsImage,
    News,
    Slaider,
    PublicOffers,
    Help,
    Footer,
    BackCall,
    )


class SlaiderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Slaider
        fields = [
            'id',
            'photo',
            ]


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = [
                'id',
                'name', 
                'get_absolute_url',
                'articul', 
                'color', 
                'price',
                'old_price',
                'discount', 
                'description', 
                'images',
                'size_row', 
                'quantity', 
                'fabric_structure', 
                'fabric', 
                'status',
                'created_at',
                'available',
                ]


class CollectionSerializer(serializers.ModelSerializer):
    # products = ProductSerializer(many=True)
    class Meta:
        model = Collection
        fields = [
            'id',
            'title',
            'photo',
            # 'products',
            ]
        depth = 1


class CategorySerializer(serializers.ModelSerializer):
    products = ProductSerializer(many=True)
    class Meta:
        model = Category
        fields = [
                'id',
                'name', 
                'get_absolute_url',
                'products',
                ]
        depth = 1


class ProductImageSerializer(serializers.ModelSerializer):
    # products = ProductSerializer(many=True)
    class Meta:
        model = ProductImage
        fields = [
                'id',
                # 'products',
                # 'image',
                ]
        depth = 1


class ProductColorSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductColor
        fields = [
                'id',
                'color',
                ]
        depth = 1


class FavoriteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Favorite
        fields = [
            'id',
            'like',
            ]
        depth = 1


class AboutUsSerializer(serializers.ModelSerializer):
    class Meta:
        model = AboutUs
        fields = [
                'id',
                'title', 
                'description',
            ]


class AboutUsImageSerializer(serializers.ModelSerializer):
    about = AboutUsSerializer(many=True)
    class Meta:
        model = AboutUsImage
        fields = [
                'id',
                'about',
                'image',
                ]
        depth = 1


class NewsSerializer(serializers.ModelSerializer):
    class Meta:
        model = News
        fields = [
            'image',
            'title',
            'description',
        ]


class AdvantagesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Advantages
        fields = [
            'icon',
            'title',
            'description',
        ]


class PublicOfferSerializer(serializers.ModelSerializer):
    class Meta:
        model = PublicOffers
        fields = [
            'id',
            'title',
            'description',
            ]


class HelpSerializer(serializers.ModelSerializer):
    class Meta:
        model = Help
        fields = [
            'id',
            'question',
            'answer',
            'photo',
            ]


class FooterSerializer(serializers.ModelSerializer): 
    class Meta:
        model = Footer
        fields = [
            'id',
            'logotype',
            'info',
            'id_header',
            'number',
            'type',
            'link_n',
            'account',
            ]


class BackCallSerializer(serializers.ModelSerializer): 
    class Meta:
        model = BackCall
        fields = [
            'id',
            'name',
            'number',
            'created_at',
            'type_of_appeal',
            'status_of_call',
            ]


class FloatingSerializer(serializers.ModelSerializer):
    class Meta:
        model = FloatingButton
        fields = [
            'id',
            'whatsapp',
            'telegram',
            ]