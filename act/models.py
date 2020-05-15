from django.db import models
from multiselectfield import MultiSelectField

class Person(models.Model):
    sex_choices = (
        ('male', 'Male'),
        ('female', 'Female')
    )
    martial_choices = (
        ('single', 'Single'),
        ('married', 'Married'),
        ('divorce', 'Divorce'),
        ('widowed', 'Widowed')
    )
    education_choices = (
        ('below matric', 'Below Matric'),
        ('matriculate', 'Matriculate'),
        ('12 pass', '12 Pass'),
        ('graduate', 'Graduate'),
        ('pg', 'PG'),
        ('ph.d', 'Ph.D'),
        ('illetrate', 'Illetrate')
    )
    occupation_choices = (
        ('student', 'Student'),
        ('govt. employee', 'Govt. Employee'),
        ('unemployed', 'Unemployed'),
        ('self-employed', 'Self-Employed'),
        ('cultivator', 'Cultivator'),
        ('pvt. employee', 'Pvt. Employee'),
        ('minial job', 'Minial Job'),
        ('others', 'Others'),
        ('pensioner', 'Pensioner'),
        ('house wife', 'House wife'),
    )
    income_choices = (
        ('nill', 'Nill'),
        ('below ₹10k', 'Below ₹10k'),
        ('₹10k to ₹25k', '₹10k to ₹25k'),
        ('₹25k to ₹50k', '₹25k to ₹50k'),
        ('above ₹50k', 'Above ₹50k')
    )

    #Details of Education Qualification

    type_choice = (
        ("government", "Government"),
        ("private", "Private"),
        ("anganwadi center", "Anganwadi Center"),
    )
    education_proximity_choice = (
        ("0-5", '0-5km'),
        ('5-10', '5-10km'),
        ('10+', 'Above 10km'),
        ('outside the state', 'Outside the state'),
    )

    # Allied Farm
    farm_type_choice = (
        ('poultry', 'Poultry'),
        ('live stock', 'Live Stock'),
        ('others', 'others')
    )

    #Bussiness
    business_type_choice = (
        ('whole sale', 'Whole Sale'),
        ('retail shop', 'Retail Shop'),
        ('others', 'others')
    )

    #Personal Info
    name = models.CharField(max_length=200)
    sex = models.CharField(choices=sex_choices, max_length=50)
    martial_status = models.CharField(choices=martial_choices, max_length=50)
    age = models.IntegerField()
    education_level = models.CharField(choices=education_choices, max_length=50)
    occupation_status = models.CharField(choices=occupation_choices, max_length=50)
    income = models.CharField(choices=income_choices, max_length=50)
    house_no = models.IntegerField()

    #"Government Documents:"
    registered_voter = models.BooleanField(default=False)
    procured_certificate_available = models.BooleanField(default=False)
    aadhar_card_available = models.BooleanField(default=False)
    bank_account_available = models.BooleanField(default=False)
    

    #"Details of Education Qualification"
    course_class = models.CharField(max_length=50, blank=True)
    type_of_education_sector = models.CharField(choices=type_choice, max_length=50, blank=True)
    education_facility_proximity = models.CharField(choices=education_proximity_choice, max_length=50, blank=True)
    satisfaction_of_study = models.BooleanField(default=False, blank=True)
    scholarship_received = models.BooleanField(default=False, blank=True)
    #"Specify the scholarship Left"
    scholarship_name = models.CharField(max_length=300, blank=True)
    drop_out = models.BooleanField(default=False, blank=True)
    #"Reason Of DropOut Left"
    drop_out_reason = models.CharField(max_length=1000, blank=True)

    

 #  EconomicActivityInGovernmentSector
    government_designation = models.CharField("Designation", max_length=100, blank=True)
    government_group = models.CharField('Group/Category', max_length=100, blank=True)
    government_monthly_income = models.IntegerField("Monthly Income",  null=True, blank=True)  

#   EconomicActivityInPrivateSector
    private_designation = models.CharField("Designation", max_length=100, blank=True)
    private_group = models.CharField('Group/Category', max_length=100, blank=True)
    private_monthly_income = models.IntegerField("Monthly Income", default=0, blank=True)

#   EconomicActivityInAgriculture
    own_agriculture_land = models.BooleanField()
    size_of_land = models.CharField(max_length=100, blank=True)
    purpose_of_land = models.CharField(max_length=1000, blank=True)
    profit = models.IntegerField("Profit from the agriculture land", default=0, blank=True)

#   Allied Farm
    farm_type = models.CharField(max_length=20, blank=True, choices=farm_type_choice)
    farm_remark = models.CharField("Remarks, If any?", max_length=1000, blank=True)

#   Business
    business_type = models.CharField(max_length=20, blank=True, choices=business_type_choice)
    business_remark = models.CharField("Remarks, If any?", max_length=1000, blank=True)
    
#   Entreprenureship    
    type_of_entreprenureship = models.CharField(max_length=1000, blank=True)
    entreprenureship_remark = models.CharField("Remarks, If any?", max_length=1000, blank=True)

    def __str__(self):
        return self.name



class Orphan(models.Model):
    person = models.ForeignKey(Person, on_delete=models.CASCADE)
    schemes = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return self.person.name


class OldAgedPerson(models.Model):
    person = models.ForeignKey(Person, on_delete=models.CASCADE)
    schemes = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return self.person.name

class DifferentlyAblePerson(models.Model):
    person = models.ForeignKey(Person, on_delete=models.CASCADE)
    types = models.CharField("Type", max_length=200, blank=True)
    schemes = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return self.person.name

class Haji(models.Model):
    person = models.ForeignKey(Person, on_delete=models.CASCADE)
    schemes = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return self.person.name


class Housing(models.Model):
    "Housing"
    house_type_choice = (
        ('pucca', 'Pucca'),
        ('semi pucca', 'Semi Pucca'),
        ('kutcha', 'Kutcha')
    )
    ownership_choice = (
        ('owned', 'Owned'),
        ('rented', 'Rented')
    )
    cooking_fuel_choices = (
        ('firewood', 'Firewood'),
        ('lpg', 'LPG'),
        ('electricity', 'Electricity'),
        ('kerosene', 'Kerosene'),
    )
    "Drinking & Sanitation"
    water_source_choice = (
        ('pipe', 'Pipe'),
        ('river', 'River'),
        ('handpump', 'Handpump'),
        ('common pond', 'Common Pond'),
        ('own pond', 'Own Pond'),
        ('others', 'Others')
    )
    water_availability_choices = (
        ('less than 1km', 'Less than 1km'),
        ('more than 1km', 'More than 1km')
    )
    toilet_facility_choice = (
        ('open', 'Open'),
        ('outlet', 'Outlet'),
        ('others', 'Others')
    )
    "Settlement"
    "Family Type"
    family_type_choice = (
        ('joint family', 'Joint Family'),
        ('nuclear family', 'Nuclear Family'),
        ('extended family', 'Extended Family')
    )
    settled_years = (
        ('since birth', 'Since Birth'),
        ('<10', 'Less than 10 years'),
        ('<25', 'Less than 25 years'),
        ('<50', 'Less than 50 years'),
        ('<70', 'Less than 70 years'),
        ('>70', 'Above 70 years'),
    )
    

    house_no = models.IntegerField("House No", unique=True)

    "HOUSING"
    head_of_family = models.CharField(max_length=100)
    homested_area = models.CharField(max_length=20)
    type_of_house = models.CharField(choices=house_type_choice, max_length=100)
    ownership = models.CharField(choices=ownership_choice, max_length=100)
    no_of_rooms = models.IntegerField()
    fuel_for_cooking = MultiSelectField(choices=cooking_fuel_choices)
    access_to_electricity = models.BooleanField(default=False)

    "Family Members"
    members = models.ManyToManyField(Person, related_name='family_members')

    "Drinking & Sanitation"
    water_source = MultiSelectField(choices=water_source_choice)
    water_availability = models.CharField(choices=water_availability_choices, max_length=100)
    toilet_facility = models.CharField(choices=toilet_facility_choice, max_length=100)
    bath_facility = models.BooleanField(default=False)
    sewage_disposal_facility= models.BooleanField(default=False)

    "Settlement"
    no_of_years_stayed_here = models.CharField(max_length=20, choices=settled_years)
    ever_lived_in_another_place = models.BooleanField(default=False)
    place_name = models.CharField('If yes, specify the place!', max_length=200, null=True, blank=True)



    "Family Type"
    family_type = models.CharField(choices=family_type_choice, max_length=100)

    "Orphan Children in The Household"
    orphan_children_available = models.BooleanField('Is there any orphan children in your household? If yes, specify how many?', default=False)
    orphan_children_names = models.ManyToManyField(Orphan, max_length=300, verbose_name='Orphan Names', blank=True, related_name='orphan_person_names')

    "Differently Able members in the Household:"
    differently_able_person_available = models.BooleanField('Are there any differently able persons in the household?', default=False)
    differently_able_person_available_names = models.ManyToManyField(DifferentlyAblePerson, blank=True, related_name='differently_able_person')

    "Aged/Old  age person  in the Household:"
    old_aged_person_available = models.BooleanField('Is there any old aged person in your household? If yes, specify below?', default=False)
    old_aged_person_names = models.ManyToManyField(OldAgedPerson, verbose_name='Old Aged Names', max_length=300, blank=True, related_name='old_person_names')
    
    "Profile on performance of Hajj"
    haji_available = models.BooleanField('Is there any Haji in the household?', default=False)
    haji_name = models.ManyToManyField(Haji, verbose_name="Haji Names", max_length=300, blank=True, related_name='haji_person_names')

    "Government Welfare Schemes:"
    priority_household_choice = (
        ('bpl', 'BPL'),
        ('apl', 'APL'),
        ('aay', 'AAY')
    )
    priority_household = models.CharField(choices=priority_household_choice, max_length=10)
    nation_food_security_act = models.BooleanField('Covered by National Food Security Act (NFSA)?')
    housing_schemes = models.BooleanField('Housing Scheme? If yes, specify below.')
    specify_housing_schemes= models.CharField(max_length=300, blank=True)
    old_aged_pension_scheme = models.BooleanField('Old aged pension scheme, If yes, specify below.')
    specify_old_aged_pension_scheme = models.CharField(max_length=300, blank=True)
    other_schemes = models.BooleanField("If other scheme, specify below.")
    specify_other_schemes = models.CharField(max_length=300, blank=True)

    def __str__(self):
        return f"{self.house_no}"

