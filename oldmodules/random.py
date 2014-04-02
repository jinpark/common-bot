"""
random.py - Phenny Random Stuff Module
Jin Park - jinpark.net

http://inamidst.com/phenny/
"""

from random import choice

FOODPORN_SLUGS = ["moist-pumpkin-spice-bundt-cake-with-caramel-cream-cheese-frosting","sea-scallop-with-truffled-cauliflower-puree-bacon-crispy-mushroom-and-creamer-potatoes","dense-fudgy-brownies-with-oreo-bits-and-ganache","toasted-pepperoni-capicola-ham-and-asiago-sandwich-with-mascarpone-and-pickled-onions-and-peppers","chewy-raspberry-lemon-pistachio-and-coffee-parisian-macarons","savory-bacon-rosemary-garlic-and-parmesan-cheese-straws","chinese-five-spice-chicken-satay","thai-chicken-empanadas-chile-poblano-oaxaca-cheese-mango-salsa","crispy-sweet-potato-fries-with-sea-salt","beef-spicy-pork-sausage-and-goat-cheese-meatballs-in-marinara-on-ciabatta","asparagus-applewood-smoked-bacon-and-point-reyes-blue-cheese","rich-espresso-chocolate-truffles","handmade-potato-gnocchi-pan-seared-with-sausage-fennel-and-tomato","grilled-strip-steak-with-sauteed-heirloom-and-grape-tomatoes-thyme-and-rosemary","fried-bologna-sandwich-on-a-pretzel-bun-with-a-sunny-side-up-egg","coconut-chocolate-chip-rice-crispy-treats","buttery-flaky-white-peach-crumb-tart","succulent-char-sui-marinated-deboned-grilled-quail","blood-orange-ginger-beer-and-tequila-cocktail","artichoke-heart-crimini-mushroom-and-meatball-soup","warm-blondie-drenched-in-hot-fudge-with-a-scoop-of-vanilla-chocolate-chip-ice-cream","fresh-sweet-lobster-roll-on-buttery-hotdog-buns","airy-chocolate-macarons-filled-with-dark-chocolate-ganache","classic-boston-cream-pie-glazed-with-ganache-and-filled-with-vanilla-cream","bread-knots-with-gruyere-bacon-rosemary","oozing-brie-and-pumpkin-quesadilla-spiced-with-sage-cayenne-and-chile-powder","maki-style-sea-urchin-with-salmon-roe-and-yuzu-tobiko-with-soy-drizzle-smoked-sea-salt-and-lime-on-himalayan-salt-brick","ripe-blackberry-and-peach-oatmeal-crumble-with-a-shortbread-crust","juicy-pork-and-beef-meatballs-a-la-pizzaiola-stuffed-with-smoked-mozzarella-in-a-hearty-red-sauce","hearty-red-wine-braised-beef-stew-with-pearl-barley","layers-of-chocolate-ganache-creamy-peanut-butter-chocolate-hazelnut","australian-marron-spinach-fennel-puree-israeli-couscous","sweet-ripe-heirloom-tomato-salad-with-basil-golden-lemon-thyme-nasturtium-and-nunez-de-prado-olive-oil","grilled-artichokes-with-thai-red-curry-beurre-blanc","coconut-cupcake-filled-with-lime-curd-topped-with-coconut-swiss-meringue-buttercream","classic-decadent-molten-chocolate-cake-dusted-with-powdered-sugar","broccoli-rabe-and-mushroom-macaroni-and-cheese-with-grilled-lobster","coppa-ham-sauteed-shiitake-garlic-pizza","bun-moc-vietnamese-style-pork-and-mushroom-noodle-soup","filet-with-gorgonzola-on-roasted-garlic-rosemary-blue-cheese-grits-with-bing-cherry-red-wine-reduction","coconut-ice-cream-swirled-with-raspberry-sauce-and-bittersweet-chocolate-chunks","ny-strip-with-creamy-polenta-stuffed-poblanos-and-rich-oaxacan","moscato-wine-poached-pear-wrapped-in-puff-pastry-drizzled-with-poaching-liquid-reduction","ranch-seasoned-roasted-potatoes-with-melted-cheddar-crumbled-smoky-bacon-and-scallions","savory-oatmeal-with-manchego-chorizo-hazelnuts-tangy-cilantro-pesto-and-a-sunny-side-up-egg","tomato-fresh-basil-and-roasted-garlic-soup-with-grilled-cheese-croutons-and-pesto","indian-potato-and-pea-filled-samosas","crispy-confit-pork-belly-w-snap-pea-puree","gooey-rich-chocolate-and-cheesecake-swirl-brownie","creamy-gruyere-sharp-cheddar-and-pecorino-romano-macaroni-and-cheese-with-bacon-and-lobster","braised-chicken-leg-with-cheesy-garlic-grits","braised-baby-artichokes-criminis-garlic-sausage-oregano","creamy-smoky-chipotle-guacamole-with-tortilla-chips","potato-leek-spinach-bacon-soup","coffee-garam-masala-crusted-sea-scallops","succulent-lobster-taco-with-pico-de-gallo-shredded-pickled-red-cabbage-and-tangy-lime-crema","meyer-lemon-curd-tarts-with-sugar-cookie-crust","grilled-chipotle-brined-butterflied-turkey","fluffy-gnocchi-baked-with-pancetta-mozzarella-and-tomato-sauce","spicy-fresh-ginger-blondie-with-ginger-salted-caramel-sauce-vanilla-bean-ice-cream-and-crystallized-ginger","shrimp-bacon-sweet-pea-puree-feta-pomegranate-tostada","creamy-roasted-garlic-and-sriracha-hummus-drizzled-with-olive-oil","eggs-en-cocotte-with-baby-spinach-mushrooms-red-peppers-garlic-and-green-onions","whiskey-marinated-ripe-peach-shortbread-bars-drizzled-with-jack-daniels-glaze","penang-asam-laksa-spicy-noodle-soup-with-flaked-mackerel-tamarind-and-pineapple","succulent-asian-style-hoisin-marinated-pork-ribs","oatmeal-chocolate-chip-cookies","moist-spongy-vanilla-cake-soaking-up-syrupy-fresh-berries-and-toasted-hazelnuts","marinated-flat-iron-steak-fajitas-with-grilled-poblano-red-pepper-and-onion","silky-roasted-strawberry-and-balsamic-ice-cream","bacon-jam-stuffed-french-toast-with-chicory-cane-syrup-and-spiced-pecans","peppercorn-crusted-sea-scallop-with-shaved-zucchini-yellow-squash-oregano","fluffy-italian-zeppole-filled-with-blueberry-compote","donuts-filled-with-maple-mousse-and-topped-with-maple-bacon-frosting-and-crumbled-bacon","savory-ground-pork-filled-cabbage-rolls-in-tomato-sauce","crispy-buttery-herb-roasted-potatoes","sweet-and-salty-dark-fudge-brownies-with-pretzel-bites-and-peanut-butter-frosting","marinated-cremini-mushrooms-and-shallots-with-homemade-vinegar-olive-oil-thyme-and-chives","cinnamon-fried-apples-sunny-side-up-egg-breakfast-sausage-and-biscuit","lemon-garlic-and-rosemary-marinated-lamb-chops","pineapple-ginger-pork-rib-chops-with-napa-cabbage-pineapple-and-daikon-slaw","grand-marnier-and-orange-juice-soaked-cake-topped-with-almonds-powdered-sugar-and-orange-zest","intense-espresso-ice-cream-tart-topped-with-shaved-dark-and-white-chocolate","soft-chewy-classic-chocolate-chip-cookies","sweet-beet-avocado-and-orange-salad-with-citrus-vinaigrette-shaved-red-onions-and-toasted-slivered-almonds","croque-madame-with-yellowtail-sashimi-prosciutto-and-sunny-side-up-quail-egg-on-brioche","butter-poached-lobster-tail-with-sous-vide-beef-tenderloin-sauteed-spinach-duck-fat-poached-creamer-potatoes","rich-creamy-new-york-style-cheese-cake-with-sweet-cherry-sauce","fluffy-brown-sugar-sweetened-mascarpone-tart-with-cinnamon-port-roasted-figs","juicy-spice-rubbed-chicken-breast","crusty-bread-stuffed-with-hot-and-sweet-italian-sausage-oven-dried","fluffy-gooey-bosc-pear-and-rosemary-upside-down-cake","flaky-buttery-hand-pies-with-rich-blueberry-filling","tender-veal-scaloppine-with-a-rich-mushroom-and-marsala-wine-sauce","creamy-humboldt-fog-goat-cheese","pineapple-coconut-apple-crisp","soft-brown-butter-salted-caramel-stuffed-toffee-chip-cookies","smokey-bbq-chicken-sliders-with-cool-crunchy-coleslaw-on-sesame-seed-buns","gising-gising-long-beans-and-minced-pork-in-a-spicy-coconut-cream-sauce","tender-potato-gnocchi-braised-lamb-ragout-with-berbere-and-preserved-lemon"];

def foodporn(phenny, input):
    phenny.say("http://foodporndaily.com/pictures/" + choice(FOODPORN_SLUGS))

foodporn.commands = ['foodporn']
foodporn.priority = 'low'
foodporn.example = '.foodporn'