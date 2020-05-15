from django.contrib import admin
from .models import (
    Person, Housing, Orphan, Haji, DifferentlyAblePerson, OldAgedPerson,
)
from django.contrib.auth.models import Group
from import_export.admin import ImportExportModelAdmin
from import_export import resources, fields
from import_export.widgets import ManyToManyWidget, ForeignKeyWidget, BooleanWidget


class PersonAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    fieldsets = [
        (
            'Personal Info', {
                'fields':[
                    'name', 'sex', 'age', 'martial_status', 'education_level', 'occupation_status', 
                    'income', 'house_no',
                ]
            
            }
        ),
        (
            'Government Documents', {
                'fields':[
                    'registered_voter', 'procured_certificate_available', 'aadhar_card_available', 
                    'bank_account_available',
                ]
            }
        ), 
        (
            'Details of Education Qualification (Age 3-23)', {
                'fields':[
                    'course_class', 'type_of_education_sector', 'education_facility_proximity', 'satisfaction_of_study',
                    'scholarship_received', 'scholarship_name', 'drop_out', 'drop_out_reason', 
                ]
            }
        ), 
        (
            'Economic Activity In Government Sector', {
                'fields':[
                    'government_designation', 'government_group', 'government_monthly_income',
                ]
            }
        ),
        (
            'Economic Activity In Private Sector', {
                'fields':[
                    'private_designation', 'private_group', 'private_monthly_income',
                ]
            }
        ), 
        (
            'Economic Activity In Agriculture', {
                'fields':[
                    'own_agriculture_land', 'purpose_of_land', 'profit',
                ]
            }
        ),
        (
            'Allied Farm', {
                'fields':[
                    'farm_type', 'farm_remark',
                ]
            }
        ),
        (
            'Business', {
                'fields':[
                    'business_type', 'business_remark',
                ]
            }
        ),
        (
            'Entreprenureship', {
                'fields':[
                    'type_of_entreprenureship', 'entreprenureship_remark',
                ]
            }
        ),
    ]


#Orphan Resource
class OrphanResource(resources.ModelResource):
    name = fields.Field(
    column_name = 'Name',
    attribute = 'person',
    widget = ForeignKeyWidget(Person, 'name')
    )

    class Meta:
        model = Orphan
        fields = ('name', 'schemes')
        export_order = ('name', 'schemes')

class OrphanAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    resource_class = OrphanResource  
    list_display = ['person',]  

#Old Aged Person Resource
class OldAgedResource(resources.ModelResource):
    name = fields.Field(
        column_name = 'Name',
        attribute = 'person', 
        widget = ForeignKeyWidget(Person, 'name')
    )

    class Meta:
        model = OldAgedPerson
        fields = ('name', 'schemes')
        export_order = ('name', 'schemes')

class OldAgedPersonAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    resource_class = OldAgedResource


#Haji Resource
class HajiResource(resources.ModelResource):
    name = fields.Field(
        column_name = 'Name',
        attribute = 'person',
        widget = ForeignKeyWidget(Person, 'name')
    )

    class Meta:
        model = Haji 
        fields = ('name', 'schemes')
        export_order = ('name', 'schemes')


class HajiAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    resource_class = HajiResource


#DifferentlyAblePerson Resource
class DiffrentAblePersonResource(resources.ModelResource):
    name = fields.Field(
        column_name = 'Name',
        attribute = 'person',
        widget = ForeignKeyWidget(Person, 'name')
    )

    class Meta:
        model = DifferentlyAblePerson 
        fields = ('name', 'schemes', 'types')
        export_order = ('name', 'types', 'schemes')


class DifferentlyAblePersonAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    resource_class = DiffrentAblePersonResource


#Housing Resource
class HousingResource(resources.ModelResource):
    orphan_children_names = fields.Field(
    column_name = 'Orphan Children',
    attribute = 'orphan_children_names',
    widget = ManyToManyWidget(Orphan, separator=',', field='person')
    )

    members = fields.Field(
    column_name = 'Family Members',
    attribute = 'members',
    widget = ManyToManyWidget(Person, separator=',', field='name')
    )

    old_aged_person_names = fields.Field(
    column_name = 'Old Aged Person Names',
    attribute = 'old_aged_person_names',
    widget = ManyToManyWidget(OldAgedPerson, separator=',', field='person')
    )

    differently_able_person_names = fields.Field(
    column_name = 'Differetly Able Person Names',
    attribute = 'differently_able_person_available_names',
    widget = ManyToManyWidget(DifferentlyAblePerson, separator=',', field='person')
    )

    haji_person = fields.Field(
    column_name = 'Hajis',
    attribute = 'haji_name',
    widget = ManyToManyWidget(Haji, separator=',', field='person')
    )

    class Meta:
        model = Housing
        fields = (
            'head_of_family', 'house_no', 'members', 'homested_area', 'type_of_house', 'ownership', 'no_of_rooms', 'fuel_for_cooking', 
            'access_to_electricity', 'water_source', 'water_availability', 'toilet_facility', 'bath_facility', 'sewage_disposal_facility', 
            'no_of_years_stayed_here', 'ever_lived_in_another_place',  'place_name','family_type', 'orphan_children_available', 'orphan_children_names',
            'differently_able_person_available', 'differently_able_person_names', 'old_aged_person_available', 'old_aged_person_names', 'haji_available',
            'haji_person', 'priority_household', 'nation_food_security_act', 'housing_schemes', 'specify_housing_schemes', 'old_aged_pension_scheme', 
            'specify_old_aged_pension_scheme', 'other_schemes', 'specify_other_schemes', 
        )
        export_order = (
            'head_of_family', 'house_no', 'members', 'homested_area', 'type_of_house', 'ownership', 'no_of_rooms', 'fuel_for_cooking', 
            'access_to_electricity', 'water_source', 'water_availability', 'toilet_facility', 'bath_facility', 'sewage_disposal_facility', 
            'no_of_years_stayed_here', 'ever_lived_in_another_place', 'place_name', 'family_type', 'orphan_children_available', 'orphan_children_names',
            'differently_able_person_available', 'differently_able_person_names', 'old_aged_person_available', 'old_aged_person_names', 'haji_available',
            'haji_person', 'priority_household', 'nation_food_security_act', 'housing_schemes', 'specify_housing_schemes', 'old_aged_pension_scheme', 
            'specify_old_aged_pension_scheme', 'other_schemes', 'specify_other_schemes', 
        )


class HousingAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    resource_class = HousingResource
    list_display = ('house_no', 'head_of_family', 'priority_household')
    list_filter = ('priority_household', 'family_type', 'ownership')
    fieldsets = [
        (
            "Housing", {
                'fields':[
                    'head_of_family',('house_no', 'homested_area', 'type_of_house', 'ownership'),
                    ('no_of_rooms', 'fuel_for_cooking', 'access_to_electricity'),
                ]
            }
        ), 
        (
            'Family Members',{
                'fields':[
                    'members',
                ]
            }
        ),
        (
            "Drinking & Sanitation", {
                'fields':[
                    'water_source', 'water_availability', 'toilet_facility',
                    'bath_facility', 'sewage_disposal_facility',
                ]
            }

        ),
        (
            "Settlement", {
                'fields':[
                    'no_of_years_stayed_here', 'ever_lived_in_another_place', 'place_name',
                ]
            }
        ),
        (
            "Family Type", {
                'fields':[
                    'family_type',
                ]
            }
        ),
        (
            "Orphan Children in The Household", {
                'fields':[
                    'orphan_children_available', 'orphan_children_names'
                ]
            }
        ),
        (
            "Differently Able members in the Household", {
                'fields':[
                    'differently_able_person_available', 'differently_able_person_available_names'
                    ]
            }
        ),
        (
            "Aged/Old  age person  in the Household", {
                'fields':[
                    'old_aged_person_available', 'old_aged_person_names'
                ]
            }
        ),
        (
            "Profile on performance of Hajj", {
                'fields':[
                    'haji_available', 'haji_name', 
                ]
            }
        ),
        (
            "Government Welfare Schemes", {
                'fields':[
                    'priority_household', 'nation_food_security_act', 'housing_schemes', 
                    'specify_housing_schemes', 'old_aged_pension_scheme', 'specify_old_aged_pension_scheme', 
                    'other_schemes', 'specify_other_schemes', 
                ]
            }
        ),
    ]

admin.site.register(Person, PersonAdmin)
admin.site.register(Housing, HousingAdmin)
admin.site.register(Orphan, OrphanAdmin)
admin.site.register(Haji, HajiAdmin)
admin.site.register(DifferentlyAblePerson, DifferentlyAblePersonAdmin)
admin.site.register(OldAgedPerson, OldAgedPersonAdmin)

#Admin Custamization
admin.site.unregister(Group)
admin.site.site_header = 'SOCIO-ECONOMIC SURVEY'
admin.site.site_title = 'SOCIO-ECONOMIC SURVEY'
admin.site.index_title = 'Survey Administration'