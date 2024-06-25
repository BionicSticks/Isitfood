from flask import Flask, request, render_template, redirect, url_for

app = Flask(__name__)

# List of foods
foods = ["apple", "bean", "nut", "seed", "banana", "orange", "grape", "pineapple", "strawberry", "strawberries",
         "blueberries", "blueberry", "raspberries", "blackberries", "cheese",
         "raspberry", "blackberry", "cherry", "mango", "peach", "plum", "pear", "apricot",
         "kiwi", "grapefruit", "lemon", "lime", "watermelon", "cantaloupe", "honeydew",
         "papaya", "guava", "fig", "date", "pomegranate", "passionfruit", "persimmon",
         "coconut", "lychee", "starfruit", "dragonfruit", "mulberry", "cranberry",
         "elderberry", "gooseberry", "currant", "tangerine", "clementine", "carrot",
         "broccoli", "cauliflower", "spinach", "kale", "lettuce", "cucumber", "zucchini",
         "eggplant", "tomato", "bell pepper", "chili pepper", "jalapeño", "potato",
         "sweet potato", "yam", "beet", "radish", "turnip", "parsnip", "onion", "garlic",
         "shallot", "leek", "green onion", "asparagus", "artichoke", "brussels sprout",
         "cabbage", "celery", "corn", "pea", "green bean", "okra", "mushroom", "pumpkin",
         "butternut squash", "acorn squash", "spaghetti squash", "kohlrabi", "rutabaga",
         "swiss chard", "bok choy", "fennel", "endive", "radicchio", "arugula", "watercress",
         "dandelion greens", "mustard greens", "collard greens", "turnip greens", "beet greens",
         "broccolini", "broccoli rabe", "snap pea", "snow pea", "chayote", "jicama",
         "seaweed", "nori", "wakame", "kombu", "dulse", "aloe vera", "bamboo shoot",
         "lotus root", "cactus", "amaranth", "quinoa", "millet", "buckwheat", "barley",
         "bulgur", "farro", "freekeh", "kamut", "spelt", "sorghum", "teff", "wheat berry",
         "wild rice", "oats", "rye", "polenta", "semolina", "wheat bran", "wheat germ",
         "chia seed", "flaxseed", "hemp seed", "pumpkin seed", "sesame seed", "sunflower seed",
         "poppy seed", "cumin seed", "fennel seed", "caraway seed", "coriander seed",
         "dill seed", "mustard seed", "celery seed", "nigella seed", "pepita", "pistachio",
         "almond", "walnut", "pecan", "hazelnut", "macadamia", "cashew", "brazil nut",
         "pine nut", "chestnut", "coconut meat", "coconut milk", "coconut water", "soybean",
         "edamame", "lentil", "chickpea", "black bean", "kidney bean", "navy bean",
         "pinto bean", "cannellini bean", "fava bean", "lima bean", "mung bean", "adzuki bean",
         "split pea", "green pea", "yellow pea", "red bean", "white bean", "black-eyed pea",
         "cranberry bean", "broad bean", "hyacinth bean", "jack bean", "scarlet runner bean",
         "snap bean", "yardlong bean", "wax bean", "butter bean", "tiger nut", "sunchoke",
         "tarwi", "vetch", "winged bean", "yam bean", "purslane", "water chestnut", "wasabi",
         "salsify", "scorzonera", "skirret", "samphire", "wood ear", "enoki", "shiitake",
         "maitake", "porcini", "morel", "chanterelle", "truffle", "feta"
         ]

# Additional foods list
additional_foods = [
    # Meats
    "chicken", "beef", "biltong", "chomps","pork", "lamb", "turkey", "duck", "goose", "quail", "rabbit",
    "venison", "bison", "buffalo", "elk", "ostrich", "pheasant", "boar", "goat",
    "kangaroo", "pigeon", "squab",

    # Fish
    "salmon", "trout", "tuna", "mackerel", "sardine", "anchovy", "herring", "cod",
    "haddock", "halibut", "flounder", "sole", "grouper", "snapper", "tilapia",
    "catfish", "bass", "perch", "walleye", "bluefish", "mahi-mahi", "swordfish",
    "marlin", "shark", "eel", "sashimi","sushi", "yellowfish", "seabass",

    # Shellfish
    "shrimp", "prawn", "lobster", "crfab", "crayfish", "scallop", "clam", "mussel",
    "oyster", "abalone", "conch", "cockle", "barnacle", "limpet", "whelk",

    # Seeds
    "chia seed", "flaxseed", "hemp seed", "pumpkin seed", "sesame seed",
    "sunflower seed", "poppy seed", "cumin seed", "fennel seed", "caraway seed",
    "coriander seed", "dill seed", "mustard seed", "celery seed", "nigella seed",

    # Cheeses
    "cheddar", "cheese", "mozzarella", "parmesan", "gouda", "swiss cheese", "brie", "camembert", "feta",
    "goat cheese","goat's cheese", "goat's milk cheese", "blue cheese", "provolone", "manchego", "gruyère", "ricotta",
    "ricotta cheese", "pecorino", "asiago", "emmental","emmentaler", "emmenthal","emmenthaler", "havarti", "taleggio",
    "fontina", "edam", "colby", "monterey jack", "stilton", "cotija", "queso"
    ]

# Append additional foods to the existing list
foods.extend(additional_foods)
#print("Total foods:", len(foods))  # This should show the increased number of items

# Initialize search history
search_history = []


def normalize_item(item):
    # Convert to lowercase
    item = item.lower()
    # Remove trailing 's' if present (for simple plural handling)
    if item.endswith('s'):
        item = item[:-1]
    return item


@app.route('/')
def index():
    return render_template('index.html', result=None, search_history=search_history)


@app.route('/check_food', methods=['POST'])
def check_food():
    item = request.form['item']
    normalized_item = normalize_item(item)
    if normalized_item in foods:
        result = "Yes, that is food."
    else:
        result = "Ewwwww don't eat that, it's not food."

    # Add the search to history
    search_history.append({'item': item, 'result': result})
    return render_template('index.html', result=result, search_history=search_history)


@app.route('/clear_history', methods=['POST'])
def clear_history():
    search_history.clear()
    return redirect(url_for('index'))


if __name__ == '__main__':
    app.run(debug=True, host='127.0.0.1', port=5000)
