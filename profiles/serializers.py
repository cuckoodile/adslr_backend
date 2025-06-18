from profiles.models import Profile, Address, Contact, Student, Guardian, Parent
from rest_framework import serializers

class AddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = Address
        fields = '__all__'


class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = '__all__'


class ProfileSerializer(serializers.ModelSerializer):
    address = AddressSerializer(many=True, read_only=True)
    contact = ContactSerializer(many=True, read_only=True)
    class Meta:
        model = Profile
        # fields = ['id', 'first_name', 'last_name', 'middle_name', 'age', 'gender', 'user', 'address', 'contact']
        fields = '__all__'


class GuardianSerializer(serializers.ModelSerializer):
    profile = ProfileSerializer(read_only=True)
    class Meta:
        model = Guardian
        fields = ['id', 'occupation', 'profile']
        depth = 1


class GetStudentSerializer(serializers.ModelSerializer):
    profile = ProfileSerializer(read_only=True)
    guardian = serializers.SerializerMethodField()

    class Meta:
        model = Student
        fields = ['id', 'birthplace', 'religion', 'profile', 'guardian']
        depth = 4

    def get_guardian(self, obj):
        guardians = obj.guardian.all()
        return GuardianSerializer(guardians, many=True).data