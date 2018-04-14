from rest_framework import serializers

from newsletter.models import Join

class Joinserializers(serializers.ModelSerializer):
    class Meta:
        model = Join
        fields = ['email']

        def validate_email(self, value):
            email = value
            qs = Join.objects.filter(email__iexact=email)
            if qs.exists():
                raise serializers.ValidationError("This email is already exist")
            return email