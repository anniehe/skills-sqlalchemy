"""

This file is the place to write solutions for the
skills assignment called skills-sqlalchemy. Remember to
consult the exercise directions for more complete
explanations of the assignment.

All classes from model.py are being imported for you
here, so feel free to refer to classes without the
[model.]User prefix.

"""

from model import *

init_app()

# -------------------------------------------------------------------
# Start here.


# Part 2: Write queries

# Get the brand with the **id** of 8.
brand_8 = Brand.query.get(8)

# Get all models with the **name** Corvette and the **brand_name** Chevrolet.
chevrolet_corvette = Model.query.filter_by(name='Corvette', brand_name='Chevrolet').all()

# Get all models that are older than 1960.
old_models = Model.query.filter(Model.year < 1960).all()

# Get all brands that were founded after 1920.
brands_after_1920 = Brand.query.filter(Brand.founded > 1920).all()

# Get all models with names that begin with "Cor".
cor_models = Model.query.filter(Model.name.like('Cor%')).all()

# Get all brands with that were founded in 1903 and that are not yet discontinued.
brands_1903 = Brand.query.filter(Brand.founded == 1903, Brand.discontinued.is_(None)).all()

# Get all brands with that are either discontinued or founded before 1950.
brands_discont_founded_before_1950 = Brand.query.filter((Brand.discontinued.isnot(None)) | (Brand.founded < 1950)).all()

# Get any model whose brand_name is not Chevrolet.
not_chevrolet = Model.query.filter(Model.brand_name != 'Chevrolet').first()

# Fill in the following functions. (See directions for more info.)


def get_model_info(year):
    '''Takes in a year, and prints out each model, brand_name, and brand
    headquarters for that year using only ONE database query.'''

    models = Model.query.filter_by(year=year).all()

    print "%-10s \t %-10s \t %-10s" % (
        "MODEL NAME", "BRAND NAME", "HEADQUARTERS")
    print "-"*11, "\t", "-"*11, "\t", "-"*20

    for model in models:
        print "%-10s \t %-10s \t %-10s" % (
            model.name, model.brand_name, model.brand.headquarters)


def get_brands_summary():
    '''Prints out each brand name, and each model name for that brand
     using only ONE database query.'''

    models = Model.query.all()

    print "BRAND SUMMARY\n"
    print "%-10s \t %-10s" % ("BRAND NAME", "MODEL NAME")
    print "-"*11 + "\t" + "-"*11

    for model in models:
        print "%-10s \t %-10s" % (model.brand_name, model.name)

# -------------------------------------------------------------------


# Part 2.5: Advanced and Optional
def search_brands_by_name(mystr):
    pass


def get_models_between(start_year, end_year):
    pass

# -------------------------------------------------------------------

# Part 3: Discussion Questions (Include your answers as comments.)

# 1. What is the returned value and datatype of ``Brand.query.filter_by(name='Ford')``?
#    The returned value and datatype is a query object.
#    It's still a "question" until the answer is fetched using .all(), .first(), or .one()
#    to return a list of records (objects).

# 2. In your own words, what is an association table, and what *type* of relationship
# does an association table manage?
#    An association table is a table that contains no meaningful data of its own and just
#    provides an association between tables. It contains foreign keys of the other
#    tables and manages the many to many relationship.
#
