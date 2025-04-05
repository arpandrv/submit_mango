# mango_app/data.py
from .data_models import MangoItem

# Create instances of pests and diseases
mango_items = [
    # Pests
    MangoItem(
        id=1,
        name="Mango Seed Weevil", 
        scientific_name="Sternochetus mangiferae", 
        description="The adult weevil is 7-9 mm long, brown-black in color. It damages the mango seed, impacting fruit quality and export potential.",
        image_path="mango_app/images/mango_seed_weevil.jpg",
        item_type="pest",
        detailed_info="The mango seed weevil is a major quarantine pest of mangoes. The adult is 7-9 mm long, brown-black in color with light patterns on its back. The female lays eggs on developing fruit, and larvae tunnel into the seed where they develop. Affected fruit show no external symptoms, making detection difficult. The pest reduces seed viability and can cause premature fruit drop. Most damage is to the seed rather than the flesh, but infestation prevents export to many countries with quarantine restrictions."
    ),
    MangoItem(
        id=2,
        name="Mango Fruit Fly", 
        scientific_name="Bactrocera dorsalis", 
        description="A serious pest that lays eggs in ripening fruit. The larvae feed on the fruit pulp, causing decay and fruit drop.",
        image_path="mango_app/images/mango_fruit_fly.jpg",
        item_type="pest",
        detailed_info="The mango fruit fly is a significant pest that affects ripening mangoes. Adult flies are about 8mm long with clear wings marked with a dark stripe along the front margin. Females lay eggs under the skin of ripening fruit. The hatched larvae (maggots) feed on the fruit pulp, causing decay and creating an entry point for secondary infections. Infested fruit often shows small puncture marks, softening, and premature dropping. The fruit fly is highly mobile and can spread rapidly. It's a major quarantine concern, restricting export opportunities for affected regions."
    ),
    MangoItem(
        id=3,
        name="Mango Leaf Hopper", 
        scientific_name="Idioscopus spp.", 
        description="Small insects that feed on plant sap from young shoots, leaves, and inflorescences.",
        image_path="mango_app/images/mango_leaf_hopper.jpg",
        item_type="pest",
        detailed_info="Mango leafhoppers are small wedge-shaped insects about 3-5mm long that feed on plant sap from young shoots, leaves, and inflorescences. They're often light green to brownish in color and can jump or fly short distances when disturbed. These pests use piercing-sucking mouthparts to extract plant sap, causing yellowing, leaf curl, and reduced vigor. Their feeding on flower panicles can result in flower drop and reduced fruit set. Additionally, they excrete honeydew which promotes the growth of sooty mold. Heavy infestations during flowering can significantly reduce yield. These pests thrive in warm, humid conditions typical of mango growing regions."
    ),
    MangoItem(
        id=4,
        name="Mango Scale Insect", 
        scientific_name="Aulacaspis tubercularis", 
        description="Small, immobile insects that attach to plant parts and feed on sap.",
        image_path="mango_app/images/mango_scale_insect.jpg",
        item_type="pest",
        detailed_info="Mango scale insects are small, immobile pests that attach themselves to leaves, branches, and sometimes fruit of mango trees. The white mango scale (Aulacaspis tubercularis) is a common species affecting mangoes. Adult females are covered with a circular or oyster-shaped waxy shield about 2-3mm in diameter, typically white or light gray. Males are smaller with an elongated covering. These insects use their piercing-sucking mouthparts to extract plant sap, causing yellowing, leaf drop, and dieback of branches in severe infestations. They can also affect fruit appearance, reducing marketability. Scale insects excrete honeydew, leading to sooty mold growth. Heavy infestations weaken trees and can reduce yields. They're difficult to control due to their protective waxy covering."
    ),
    
    # Diseases
    MangoItem(
        id=5,
        name="Anthracnose", 
        scientific_name="Colletotrichum gloeosporioides", 
        description="A fungal disease affecting mangoes in all growth stages, particularly in humid conditions.",
        image_path="mango_app/images/anthracnose.jpg",
        item_type="disease",
        detailed_info="Anthracnose is a major fungal disease of mangoes caused by Colletotrichum gloeosporioides. It affects leaves, flowers, and fruits at all stages of development. On leaves, it appears as irregular dark spots that may coalesce and cause defoliation. On flowers, it causes blackening and blossom blight, reducing fruit set. On developing fruit, it creates small, dark, sunken spots that remain dormant until ripening, when they enlarge and cause fruit rot. Mature fruit can develop large, sunken, dark lesions with pinkish-orange spore masses in humid conditions. The disease is favored by warm, wet weather and can cause significant losses in both yield and quality. It's particularly problematic in humid tropical and subtropical regions."
    ),
    MangoItem(
        id=6,
        name="Powdery Mildew", 
        scientific_name="Oidium mangiferae", 
        description="A fungal disease that affects flowers and young fruits, causing significant yield loss.",
        image_path="mango_app/images/powdery_mildew.jpg",
        item_type="disease",
        detailed_info="Powdery mildew in mangoes is caused by the fungus Oidium mangiferae. It primarily affects inflorescences (flower panicles), young fruits, and new leaves. The disease appears as a white, powdery coating on affected plant parts. Infected flowers may dry up and fall off, significantly reducing fruit set. Young fruits may be distorted, stunted, or drop prematurely if infected. The disease can cause up to 80% yield loss in severe cases. Unlike many fungal diseases, powdery mildew can develop in relatively dry conditions with high humidity, though free water inhibits spore germination. It's particularly severe during flowering and fruit set periods when temperatures are moderate (20-25°C). The disease spreads rapidly via airborne spores."
    ),
    MangoItem(
        id=7,
        name="Bacterial Black Spot", 
        scientific_name="Xanthomonas campestris pv. mangiferaeindicae", 
        description="A bacterial disease that causes black lesions on leaves, stems, and fruits.",
        image_path="mango_app/images/bacterial_black_spot.jpg",
        item_type="disease",
        detailed_info="Bacterial black spot, caused by Xanthomonas campestris pv. mangiferaeindicae, is a serious disease affecting mangoes in many growing regions. On leaves, it appears as small, angular, water-soaked lesions that become black, necrotic spots with yellow halos. These can coalesce during severe infections, causing leaf blight. On stems and branches, it causes raised black lesions that may crack and exude gum. Fruit symptoms include small, black, raised spots that may develop into corky, star-shaped cracks with bacterial ooze. The disease reduces tree vigor, fruit quality, and marketability. It spreads through rain splash, wind-driven rain, and contaminated plant material. Warm temperatures (25-30°C) and high humidity favor disease development. It's particularly severe in wet tropical and subtropical regions."
    )
]

# Function to get item by ID
def get_item_by_id(item_id):
    """
    Retrieve a mango item by its ID
    
    Args:
        item_id (int): The ID of the item to retrieve
        
    Returns:
        MangoItem: The matching item or None if not found
    """
    for item in mango_items:
        if item.id == item_id:
            return item
    return None

# Get pests only
def get_pests():
    """Return a list of pest items only"""
    return [item for item in mango_items if item.item_type == 'pest']

# Get diseases only
def get_diseases():
    """Return a list of disease items only"""
    return [item for item in mango_items if item.item_type == 'disease']