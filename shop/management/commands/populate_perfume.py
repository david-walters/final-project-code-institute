from django.core.management.base import BaseCommand
from shop.models import Perfume

class Command(BaseCommand):
    help = 'Populates the database with initial perfume data'

    def handle(self, *args, **kwargs): # noqa
        perfumes = [
            {
                "name": "Amber Oud",
                "size": "25 ml",
                "description": "A seductive fragrance that blends spicy notes of ginger and cardamom with sweet tobacco and honey. The heart notes feature saffron and pink peppercorn.",
                "image_url": "https://ibb.co/DgRd2Xz",
                "gender": "M",
            },
            {
                "name": "White Musk",
                "size": "25 ml",
                "description": "Our White has notes of aldehydes, jasmine and floral tones, sensual and clean notes that will leave you feeling empowered to express yourself.",
                "image_url": "https://ibb.co/MBjt5qm",
                "gender": "M",
            },
            {
                "name": "Ocean Wave",
                "size": "25 ml",
                "description": "A fresh marine accord opening with bergamot and mandarin, leading to a watery floral heart of ozone, waterlily, jasmine, on a base of cedar, amber and musk.",
                "image_url": "https://ibb.co/YLWps0V",
                "gender": "M",
            },
            {
                "name": "Enigma",
                "size": "25 ml",
                "description": "Fresh grapefruit tones leads to an aromatic heart of pepper and nutmeg before settling on a deep, woody base.",
                "image_url": "https://ibb.co/F7cdzKM",
                "gender": "M",
            },
            {
                "name": "Arabian Nights",
                "size": "25 ml",
                "description": "This elixir of fruity blackcurrant, bergamot and lotus flower blends with creamy chocolate accord for the ultimate, everyday indulgence.",
                "image_url": "https://ibb.co/yXC83Q5",
                "gender": "M",
            },
            {
                "name": "Sweet Amor",
                "size": "25 ml",
                "description": "A delicious burst of citrusy notes combine with an unforgettable earthy base, giving a deep sensuality and romantic charm.",
                "image_url": "https://ibb.co/VWrj9fx",
                "gender": "F",
            },
            {
                "name": "Sunkiss",
                "size": "25 ml",
                "description": "With every dab of this immersive fragrance, you’ll experience exotic floral notes, entwined with addictive cinnamon, sandalwood and spicy saffron accords.",
                "image_url": "http://ibb.co/wJYh5rS",
                "gender": "F",
            },
            {
                "name": "Rose Essence",
                "size": "25 ml",
                "description": "The floral scent opens with deep rose, leading to trailing honeysuckle that’s decadently sweet. The vanilla, amber and musk base gives a sensual, glowing warmth",
                "image_url": "https://ibb.co/YZt8s9c",
                "gender": "F",
            },
            {
                "name": "Bluebell Necter",
                "size": "25 ml",
                "description": "A soft floral opening with earthy vetiver blooming at its irresistible heart for a deeply grounding feel. A cocooning amber base elevates this scent giving a hearty, indulgent finish.",
                "image_url": "https://ibb.co/HGhCLVp",
                "gender": "F",
            },
            {
                "name": "Angelic Touch",
                "size": "25 ml",
                "description": "Musk perfume oil, lending an inspiring positivity of floral richness. A frankincense and myrrh base illuminates the entire fragrance with an enveloping warmth and musky end.",
                "image_url": "https://ibb.co/2SNX917",
                "gender": "F",
            },
        ]

        for perfume_data in perfumes:
            perfume, created = Perfume.objects.get_or_create(
                name=perfume_data["name"],
                size=perfume_data["size"],
                defaults={
                    "description": perfume_data["description"],
                    "image_url": perfume_data["image_url"],
                    "gender": perfume_data["gender"],
                },
            )
            if created:
                self.stdout.write(self.style.SUCCESS(f'Added: {perfume.name}'))
            else:
                self.stdout.write(self.style.WARNING(f'Skipped (already exists): {perfume.name}'))
