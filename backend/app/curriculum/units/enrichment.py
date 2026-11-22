"""Visual enrichment topics: photosynthesis and the human brain.

These two are explicitly *not* part of the seven-unit course list. They are extra
illustrated topics that support the biology units, and the seed marks them as enrichment
so the interface can label them honestly.
"""

UNITS: tuple[dict, ...] = (
    {
        "number": 101,
        "category": "enrichment",
        "is_enrichment": True,
        "title_en": "Photosynthesis: How Leaves Make Food",
        "title_kn": "ದ್ಯುತಿಸಂಶ್ಲೇಷಣೆ: ಎಲೆಗಳು ಆಹಾರ ತಯಾರಿಸುವ ಬಗೆ",
        "summary_en": (
            "An illustrated walkthrough of how a green leaf uses sunlight, water and carbon "
            "dioxide to make glucose and release oxygen."
        ),
        "summary_kn": (
            "ಹಸಿರು ಎಲೆ ಸೂರ್ಯನ ಬೆಳಕು, ನೀರು ಮತ್ತು ಇಂಗಾಲದ ಡೈಆಕ್ಸೈಡ್ "
            "ಬಳಸಿ ಗ್ಲೂಕೋಸ್ ತಯಾರಿಸಿ ಆಮ್ಲಜನಕ ಬಿಡುಗಡೆ ಮಾಡುವ ಬಗೆಯ "
            "ಚಿತ್ರಿತ ವಿವರಣೆ."
        ),
        "estimated_minutes": 30,
        "visualizations": ["photosynthesis"],
        "topics": [
            {
                "title_en": "What photosynthesis is",
                "title_kn": "ದ್ಯುತಿಸಂಶ್ಲೇಷಣೆ ಎಂದರೇನು",
                "objectives_en": [
                    "State the word equation for photosynthesis.",
                    "Name the parts of the plant that take part.",
                ],
                "objectives_kn": [
                    "ದ್ಯುತಿಸಂಶ್ಲೇಷಣೆಯ ಪದ ಸಮೀಕರಣವನ್ನು ಹೇಳುವುದು.",
                    "ಇದರಲ್ಲಿ ಭಾಗವಹಿಸುವ ಸಸ್ಯದ ಭಾಗಗಳನ್ನು ಹೆಸರಿಸುವುದು.",
                ],
                "body_en": [
                    "Photosynthesis is the process by which a green plant makes its own food. "
                    "Water drawn up by the roots and carbon dioxide taken in through tiny pores in "
                    "the leaf are joined, using energy from sunlight, to form glucose. Oxygen is "
                    "released as a by-product. In words: carbon dioxide + water, in the presence "
                    "of light and chlorophyll, gives glucose + oxygen.",
                    "The green colour comes from chlorophyll, a pigment inside cell structures "
                    "called chloroplasts. Because chlorophyll absorbs red and blue light and "
                    "reflects green, leaves look green to us. Only the parts of a plant that "
                    "contain chlorophyll can photosynthesise, which is why a white or yellow patch "
                    "on a leaf makes no food.",
                ],
                "body_kn": [
                    "ದ್ಯುತಿಸಂಶ್ಲೇಷಣೆ ಎಂದರೆ ಹಸಿರು ಸಸ್ಯ ತನ್ನ ಆಹಾರವನ್ನು ತಾನೇ "
                    "ತಯಾರಿಸಿಕೊಳ್ಳುವ ಪ್ರಕ್ರಿಯೆ. ಬೇರುಗಳು ಎಳೆದುಕೊಳ್ಳುವ ನೀರು ಮತ್ತು "
                    "ಎಲೆಯ ಸಣ್ಣ ರಂಧ್ರಗಳ ಮೂಲಕ ಒಳಬರುವ ಇಂಗಾಲದ ಡೈಆಕ್ಸೈಡ್ "
                    "ಸೂರ್ಯನ ಬೆಳಕಿನ ಶಕ್ತಿ ಬಳಸಿ ಗ್ಲೂಕೋಸ್ ಆಗಿ ಸೇರುತ್ತವೆ. "
                    "ಆಮ್ಲಜನಕ ಉಪೋತ್ಪನ್ನವಾಗಿ ಬಿಡುಗಡೆಯಾಗುತ್ತದೆ. ಪದಗಳಲ್ಲಿ: "
                    "ಇಂಗಾಲದ ಡೈಆಕ್ಸೈಡ್ + ನೀರು, ಬೆಳಕು ಮತ್ತು ಕ್ಲೋರೊಫಿಲ್ "
                    "ಇರುವಾಗ, ಗ್ಲೂಕೋಸ್ + ಆಮ್ಲಜನಕ ಕೊಡುತ್ತದೆ.",
                    "ಹಸಿರು ಬಣ್ಣ ಕ್ಲೋರೊಫಿಲ್ ಎಂಬ ವರ್ಣದ್ರವ್ಯದಿಂದ ಬರುತ್ತದೆ; ಇದು "
                    "ಕ್ಲೋರೊಪ್ಲಾಸ್ಟ್ ಎಂಬ ಕಣ ರಚನೆಗಳಲ್ಲಿ ಇರುತ್ತದೆ. "
                    "ಕ್ಲೋರೊಫಿಲ್ ಕೆಂಪು ಮತ್ತು ನೀಲಿ ಬೆಳಕನ್ನು ಹೀರಿಕೊಂಡು ಹಸಿರನ್ನು "
                    "ಪ್ರತಿಫಲಿಸುವುದರಿಂದ ಎಲೆಗಳು ನಮಗೆ ಹಸಿರಾಗಿ ಕಾಣುತ್ತವೆ. "
                    "ಕ್ಲೋರೊಫಿಲ್ ಇರುವ ಭಾಗಗಳು ಮಾತ್ರ ದ್ಯುತಿಸಂಶ್ಲೇಷಣೆ "
                    "ಮಾಡಬಲ್ಲವು; ಆದ್ದರಿಂದ ಎಲೆಯ ಬಿಳಿ ಅಥವಾ ಹಳದಿ ಚುಕ್ಕೆ "
                    "ಆಹಾರ ತಯಾರಿಸಲಾರದು.",
                ],
                "key_terms": [
                    {
                        "kn": "ದ್ಯುತಿಸಂಶ್ಲೇಷಣೆ",
                        "en": "Photosynthesis",
                        "meaning_kn": "ಬೆಳಕಿನ ಶಕ್ತಿಯಿಂದ ಸಸ್ಯ ಆಹಾರ ತಯಾರಿಸುವ ಪ್ರಕ್ರಿಯೆ.",
                        "meaning_en": "The process by which plants make food using light energy.",
                    },
                    {
                        "kn": "ಕ್ಲೋರೊಫಿಲ್",
                        "en": "Chlorophyll",
                        "meaning_kn": "ಎಲೆಗೆ ಹಸಿರು ಬಣ್ಣ ಕೊಡುವ, ಬೆಳಕನ್ನು ಹೀರುವ ವರ್ಣದ್ರವ್ಯ.",
                        "meaning_en": "The green pigment that absorbs light.",
                    },
                    {
                        "kn": "ಪತ್ರರಂಧ್ರ",
                        "en": "Stomata",
                        "meaning_kn": "ಎಲೆಯ ಮೇಲ್ಮೈಯಲ್ಲಿನ ಸಣ್ಣ ರಂಧ್ರಗಳು; ಅನಿಲ ವಿನಿಮಯ ನಡೆಯುತ್ತದೆ.",
                        "meaning_en": "Tiny pores on a leaf where gases are exchanged.",
                    },
                ],
                "example_en": (
                    "A potted plant kept in a dark cupboard for a week turns pale and stops "
                    "growing: without light it cannot make glucose, even though it has water and "
                    "air."
                ),
                "example_kn": (
                    "ಒಂದು ವಾರ ಕತ್ತಲ ಕಪಾಟಿನಲ್ಲಿಟ್ಟ ಗಿಡ ಬಿಳಿಚಿಕೊಂಡು ಬೆಳೆಯುವುದನ್ನು "
                    "ನಿಲ್ಲಿಸುತ್ತದೆ: ನೀರು ಮತ್ತು ಗಾಳಿ ಇದ್ದರೂ ಬೆಳಕಿಲ್ಲದೆ "
                    "ಗ್ಲೂಕೋಸ್ ತಯಾರಿಸಲಾಗದು."
                ),
            },
            {
                "title_en": "The raw materials and the route they take",
                "title_kn": "ಕಚ್ಚಾ ವಸ್ತುಗಳು ಮತ್ತು ಅವುಗಳ ಮಾರ್ಗ",
                "objectives_en": [
                    "Trace water from root to leaf.",
                    "Explain how carbon dioxide enters and oxygen leaves.",
                ],
                "objectives_kn": [
                    "ಬೇರಿನಿಂದ ಎಲೆಯವರೆಗೆ ನೀರಿನ ಮಾರ್ಗವನ್ನು ವಿವರಿಸುವುದು.",
                    "ಇಂಗಾಲದ ಡೈಆಕ್ಸೈಡ್ ಒಳಬರುವುದು ಮತ್ತು ಆಮ್ಲಜನಕ "
                    "ಹೊರಹೋಗುವುದನ್ನು ವಿವರಿಸುವುದು.",
                ],
                "body_en": [
                    "Root hair cells absorb water and dissolved minerals from the soil. The water "
                    "travels up through narrow tubes called xylem, pulled partly by the loss of "
                    "water vapour from the leaves. It arrives at the leaf through the veins.",
                    "Carbon dioxide enters the leaf through stomata, small openings mostly on the "
                    "lower surface. Each stoma is guarded by two bean-shaped guard cells that swell "
                    "to open it and shrink to close it, which lets the plant save water on a hot "
                    "dry day. Oxygen made during photosynthesis leaves through the same stomata. "
                    "This two-way traffic is called gaseous exchange.",
                ],
                "body_kn": [
                    "ಬೇರು ಕೂದಲಿನ ಜೀವಕೋಶಗಳು ಮಣ್ಣಿನಿಂದ ನೀರು ಮತ್ತು ಕರಗಿದ "
                    "ಖನಿಜಗಳನ್ನು ಹೀರಿಕೊಳ್ಳುತ್ತವೆ. ನೀರು ಕ್ಸೈಲಂ ಎಂಬ ಸಣ್ಣ "
                    "ನಾಳಗಳ ಮೂಲಕ ಮೇಲಕ್ಕೆ ಸಾಗುತ್ತದೆ; ಎಲೆಗಳಿಂದ ನೀರಿನ ಆವಿ "
                    "ಕಳೆದುಹೋಗುವುದು ಇದಕ್ಕೆ ಸ್ವಲ್ಪ ಸಹಾಯ ಮಾಡುತ್ತದೆ. ನೀರು "
                    "ಎಲೆಯನ್ನು ನಾಳಗಳ ಮೂಲಕ ತಲುಪುತ್ತದೆ.",
                    "ಇಂಗಾಲದ ಡೈಆಕ್ಸೈಡ್ ಎಲೆಯೊಳಗೆ ಪತ್ರರಂಧ್ರಗಳ ಮೂಲಕ "
                    "ಬರುತ್ತದೆ; ಇವು ಹೆಚ್ಚಾಗಿ ಎಲೆಯ ಕೆಳಮೇಲ್ಮೈಯಲ್ಲಿರುವ ಸಣ್ಣ "
                    "ರಂಧ್ರಗಳು. ಪ್ರತಿ ರಂಧ್ರವನ್ನು ಬೀನ್ ಆಕಾರದ ಎರಡು ರಕ್ಷಕ "
                    "ಜೀವಕೋಶಗಳು ನಿಯಂತ್ರಿಸುತ್ತವೆ; ಅವು ಉಬ್ಬಿದಾಗ ರಂಧ್ರ ತೆರೆಯುತ್ತದೆ, "
                    "ಸುಕ್ಕುಗಟ್ಟಿದಾಗ ಮುಚ್ಚುತ್ತದೆ. ಇದರಿಂದ ಬಿಸಿ ಒಣ ದಿನದಲ್ಲಿ "
                    "ಸಸ್ಯ ನೀರನ್ನು ಉಳಿಸುತ್ತದೆ. ದ್ಯುತಿಸಂಶ್ಲೇಷಣೆಯಲ್ಲಿ "
                    "ತಯಾರಾದ ಆಮ್ಲಜನಕ ಅದೇ ರಂಧ್ರಗಳ ಮೂಲಕ ಹೊರಹೋಗುತ್ತದೆ. "
                    "ಈ ಎರಡು ದಿಕ್ಕಿನ ವಿನಿಮಯಕ್ಕೆ ಅನಿಲ ವಿನಿಮಯ ಎನ್ನುತ್ತಾರೆ.",
                ],
                "key_terms": [
                    {
                        "kn": "ಕ್ಸೈಲಂ",
                        "en": "Xylem",
                        "meaning_kn": "ಬೇರಿನಿಂದ ಎಲೆಗೆ ನೀರನ್ನು ಸಾಗಿಸುವ ನಾಳ.",
                        "meaning_en": "The tube that carries water from root to leaf.",
                    },
                    {
                        "kn": "ರಕ್ಷಕ ಜೀವಕೋಶ",
                        "en": "Guard cell",
                        "meaning_kn": "ಪತ್ರರಂಧ್ರವನ್ನು ತೆರೆಯುವ, ಮುಚ್ಚುವ ಜೀವಕೋಶ.",
                        "meaning_en": "A cell that opens and closes a stoma.",
                    },
                ],
                "example_en": (
                    "A leaf sealed inside a clear plastic bag on a sunny day collects water droplets "
                    "on the inside: that water vapour left the leaf through its stomata."
                ),
                "example_kn": (
                    "ಬಿಸಿಲಿನ ದಿನದಂದು ಪಾರದರ್ಶಕ ಪ್ಲಾಸ್ಟಿಕ್ ಚೀಲದಲ್ಲಿ ಮುಚ್ಚಿಟ್ಟ "
                    "ಎಲೆಯ ಒಳಭಾಗದಲ್ಲಿ ನೀರಿನ ಹನಿಗಳು ಸೇರುತ್ತವೆ: ಆ ನೀರಿನ ಆವಿ "
                    "ಎಲೆಯ ಪತ್ರರಂಧ್ರಗಳ ಮೂಲಕ ಹೊರಬಂದದ್ದು."
                ),
            },
            {
                "title_en": "Why photosynthesis matters",
                "title_kn": "ದ್ಯುತಿಸಂಶ್ಲೇಷಣೆ ಏಕೆ ಮುಖ್ಯ",
                "objectives_en": [
                    "Connect photosynthesis to food chains and to the oxygen we breathe.",
                    "Explain why plants store food as starch.",
                ],
                "objectives_kn": [
                    "ದ್ಯುತಿಸಂಶ್ಲೇಷಣೆಯನ್ನು ಆಹಾರ ಸರಪಳಿ ಮತ್ತು ನಾವು "
                    "ಉಸಿರಾಡುವ ಆಮ್ಲಜನಕಕ್ಕೆ ಜೋಡಿಸುವುದು.",
                    "ಸಸ್ಯಗಳು ಆಹಾರವನ್ನು ಪಿಷ್ಟವಾಗಿ ಸಂಗ್ರಹಿಸುವುದು ಏಕೆ "
                    "ಎಂಬುದನ್ನು ವಿವರಿಸುವುದು.",
                ],
                "body_en": [
                    "Almost every food chain begins with photosynthesis. The glucose a plant makes "
                    "is used for its own growth or stored as starch in roots, stems, seeds and "
                    "fruits. When we eat rice, wheat, potato or fruit we are eating stored plant "
                    "food, and when we eat an animal we are eating food that came from plants.",
                    "Photosynthesis also maintains the oxygen in the air we breathe. The oxygen "
                    "released by green plants, algae and tiny ocean phytoplankton is what keeps the "
                    "atmosphere breathable. A useful check: a leaf that has been in sunlight "
                    "contains starch and turns blue-black with iodine solution, while a leaf kept "
                    "in the dark does not, showing that light is needed for food production.",
                ],
                "body_kn": [
                    "ಬಹುತೇಕ ಎಲ್ಲಾ ಆಹಾರ ಸರಪಳಿಗಳು ದ್ಯುತಿಸಂಶ್ಲೇಷಣೆಯಿಂದ "
                    "ಆರಂಭವಾಗುತ್ತವೆ. ಸಸ್ಯ ತಯಾರಿಸುವ ಗ್ಲೂಕೋಸ್ ಅದರ ಬೆಳವಣಿಗೆಗೆ "
                    "ಬಳಕೆಯಾಗುತ್ತದೆ ಅಥವಾ ಬೇರು, ಕಾಂಡ, ಬೀಜ ಮತ್ತು ಹಣ್ಣುಗಳಲ್ಲಿ "
                    "ಪಿಷ್ಟವಾಗಿ ಸಂಗ್ರಹವಾಗುತ್ತದೆ. ನಾವು ಅಕ್ಕಿ, ಗೋಧಿ, ಆಲೂಗಡ್ಡೆ "
                    "ಅಥವಾ ಹಣ್ಣು ತಿನ್ನುವಾಗ ಸಸ್ಯ ಸಂಗ್ರಹಿಸಿದ ಆಹಾರವನ್ನೇ "
                    "ತಿನ್ನುತ್ತೇವೆ; ಪ್ರಾಣಿಯನ್ನು ತಿನ್ನುವಾಗ ಸಸ್ಯದಿಂದ ಬಂದ "
                    "ಆಹಾರವನ್ನೇ ತಿನ್ನುತ್ತೇವೆ.",
                    "ದ್ಯುತಿಸಂಶ್ಲೇಷಣೆ ನಾವು ಉಸಿರಾಡುವ ಗಾಳಿಯಲ್ಲಿನ "
                    "ಆಮ್ಲಜನಕವನ್ನೂ ಕಾಪಾಡುತ್ತದೆ. ಹಸಿರು ಸಸ್ಯ, ಆಲ್ಗೆ ಮತ್ತು "
                    "ಸಮುದ್ರದ ಸಣ್ಣ ಫೈಟೋಪ್ಲ್ಯಾಂಕ್ಟನ್ ಬಿಡುಗಡೆ ಮಾಡುವ "
                    "ಆಮ್ಲಜನಕವೇ ವಾತಾವರಣವನ್ನು ಉಸಿರಾಡಲು ಯೋಗ್ಯವಾಗಿ "
                    "ಇರಿಸುತ್ತದೆ. ಒಂದು ಉಪಯುಕ್ತ ಪರೀಕ್ಷೆ: ಬಿಸಿಲಿನಲ್ಲಿದ್ದ ಎಲೆಯಲ್ಲಿ "
                    "ಪಿಷ್ಟ ಇರುತ್ತದೆ ಮತ್ತು ಅಯೋಡಿನ್ ದ್ರಾವಣದಿಂದ ನೀಲಿ-ಕಪ್ಪು "
                    "ಬಣ್ಣಕ್ಕೆ ತಿರುಗುತ್ತದೆ; ಕತ್ತಲಿನಲ್ಲಿಟ್ಟ ಎಲೆ ಹಾಗಾಗುವುದಿಲ್ಲ. "
                    "ಆಹಾರ ತಯಾರಿಕೆಗೆ ಬೆಳಕು ಬೇಕು ಎಂಬುದನ್ನು ಇದು ತೋರಿಸುತ್ತದೆ.",
                ],
                "key_terms": [
                    {
                        "kn": "ಗ್ಲೂಕೋಸ್",
                        "en": "Glucose",
                        "meaning_kn": "ದ್ಯುತಿಸಂಶ್ಲೇಷಣೆಯಲ್ಲಿ ತಯಾರಾಗುವ ಸರಳ ಸಕ್ಕರೆ.",
                        "meaning_en": "The simple sugar produced by photosynthesis.",
                    },
                    {
                        "kn": "ಪಿಷ್ಟ",
                        "en": "Starch",
                        "meaning_kn": "ಸಸ್ಯಗಳಲ್ಲಿ ಆಹಾರ ಸಂಗ್ರಹದ ರೂಪ.",
                        "meaning_en": "The storage form of food in plants.",
                    },
                ],
                "example_en": (
                    "Potatoes are swollen underground stems full of stored starch: they are the "
                    "plant's saved photosynthesis from the previous season."
                ),
                "example_kn": (
                    "ಆಲೂಗಡ್ಡೆ ಎಂದರೆ ಪಿಷ್ಟ ತುಂಬಿದ, ನೆಲದೊಳಗಿನ ಉಬ್ಬಿದ "
                    "ಕಾಂಡ: ಅದು ಹಿಂದಿನ ಹಂಗಾಮಿನಲ್ಲಿ ಸಸ್ಯ ಸಂಗ್ರಹಿಸಿಟ್ಟ "
                    "ದ್ಯುತಿಸಂಶ್ಲೇಷಣೆಯ ಫಲ."
                ),
            },
        ],
        "notes_en": [
            "Word equation: carbon dioxide + water --light, chlorophyll--> glucose + oxygen.",
            "Chlorophyll in chloroplasts traps light; it reflects green and absorbs red and blue.",
            "Water is absorbed by roots and carried up in xylem.",
            "Carbon dioxide enters and oxygen leaves through stomata, mostly on the lower surface.",
            "Glucose is used for growth or stored as starch.",
            "Photosynthesis begins most food chains and maintains atmospheric oxygen.",
            "Iodine turns blue-black where starch is present — evidence that light was available.",
        ],
        "notes_kn": [
            "ಪದ ಸಮೀಕರಣ: ಇಂಗಾಲದ ಡೈಆಕ್ಸೈಡ್ + ನೀರು --ಬೆಳಕು, ಕ್ಲೋರೊಫಿಲ್--> ಗ್ಲೂಕೋಸ್ + ಆಮ್ಲಜನಕ.",
            "ಕ್ಲೋರೊಪ್ಲಾಸ್ಟ್‌ನಲ್ಲಿನ ಕ್ಲೋರೊಫಿಲ್ ಬೆಳಕನ್ನು ಹಿಡಿಯುತ್ತದೆ; ಹಸಿರನ್ನು ಪ್ರತಿಫಲಿಸಿ ಕೆಂಪು, ನೀಲಿ ಹೀರಿಕೊಳ್ಳುತ್ತದೆ.",
            "ನೀರನ್ನು ಬೇರು ಹೀರಿಕೊಂಡು ಕ್ಸೈಲಂನಲ್ಲಿ ಮೇಲಕ್ಕೆ ಸಾಗಿಸುತ್ತದೆ.",
            "ಇಂಗಾಲದ ಡೈಆಕ್ಸೈಡ್ ಒಳಬಂದು ಆಮ್ಲಜನಕ ಹೊರಹೋಗುವುದು ಪತ್ರರಂಧ್ರಗಳ ಮೂಲಕ; ಹೆಚ್ಚಾಗಿ ಕೆಳಮೇಲ್ಮೈಯಲ್ಲಿ.",
            "ಗ್ಲೂಕೋಸ್ ಬೆಳವಣಿಗೆಗೆ ಬಳಕೆಯಾಗುತ್ತದೆ ಅಥವಾ ಪಿಷ್ಟವಾಗಿ ಸಂಗ್ರಹವಾಗುತ್ತದೆ.",
            "ದ್ಯುತಿಸಂಶ್ಲೇಷಣೆ ಬಹುತೇಕ ಆಹಾರ ಸರಪಳಿಗಳನ್ನು ಆರಂಭಿಸಿ ವಾತಾವರಣದ ಆಮ್ಲಜನಕ ಕಾಪಾಡುತ್ತದೆ.",
            "ಪಿಷ್ಟ ಇರುವಲ್ಲಿ ಅಯೋಡಿನ್ ನೀಲಿ-ಕಪ್ಪು ಆಗುತ್ತದೆ — ಬೆಳಕು ಸಿಕ್ಕಿದ್ದಕ್ಕೆ ಸಾಕ್ಷ್ಯ.",
        ],
        "videos": [
            {
                "title": "ದ್ಯುತಿಸಂಶ್ಲೇಷಣೆ — ಕನ್ನಡ ವಿವರಣೆ",
                "language": "kn",
                "topic": "Photosynthesis",
                "search_query": "ದ್ಯುತಿಸಂಶ್ಲೇಷಣೆ ಕನ್ನಡ 8ನೇ ತರಗತಿ ವಿಜ್ಞಾನ ಎಲೆ ಆಹಾರ",
            },
            {
                "title": "Photosynthesis for Class 8",
                "language": "en",
                "topic": "Photosynthesis",
                "search_query": "photosynthesis class 8 explanation chlorophyll stomata stomata experiment",
            },
        ],
        "quiz": [
            {
                "question_en": "Which gas is released during photosynthesis?",
                "question_kn": "ದ್ಯುತಿಸಂಶ್ಲೇಷಣೆಯಲ್ಲಿ ಯಾವ ಅನಿಲ ಬಿಡುಗಡೆಯಾಗುತ್ತದೆ?",
                "options_en": ["Carbon dioxide", "Nitrogen", "Oxygen", "Hydrogen"],
                "options_kn": ["ಇಂಗಾಲದ ಡೈಆಕ್ಸೈಡ್", "ಸಾರಜನಕ", "ಆಮ್ಲಜನಕ", "ಹೈಡ್ರೋಜನ್"],
                "correct_index": 2,
                "explanation_en": (
                    "Oxygen is the by-product of splitting water during photosynthesis, and it "
                    "leaves through the stomata."
                ),
                "explanation_kn": (
                    "ದ್ಯುತಿಸಂಶ್ಲೇಷಣೆಯಲ್ಲಿ ನೀರು ಒಡೆದಾಗ ಆಮ್ಲಜನಕ "
                    "ಉಪೋತ್ಪನ್ನವಾಗಿ ಬರುತ್ತದೆ; ಅದು ಪತ್ರರಂಧ್ರಗಳ ಮೂಲಕ "
                    "ಹೊರಹೋಗುತ್ತದೆ."
                ),
                "difficulty": 1,
            },
            {
                "question_en": "Water reaches the leaf through the…",
                "question_kn": "ನೀರು ಎಲೆಯನ್ನು ತಲುಪುವುದು ಯಾವ ಮೂಲಕ?",
                "options_en": ["Stomata", "Xylem", "Chloroplast", "Guard cells"],
                "options_kn": ["ಪತ್ರರಂಧ್ರ", "ಕ್ಸೈಲಂ", "ಕ್ಲೋರೊಪ್ಲಾಸ್ಟ್", "ರಕ್ಷಕ ಜೀವಕೋಶ"],
                "correct_index": 1,
                "explanation_en": (
                    "Xylem is the water-conducting tissue that carries water from the roots up to "
                    "the leaves."
                ),
                "explanation_kn": (
                    "ಕ್ಸೈಲಂ ನೀರನ್ನು ಸಾಗಿಸುವ ಅಂಗಾಂಶ; ಬೇರಿನಿಂದ ಎಲೆಗೆ "
                    "ನೀರನ್ನು ಒಯ್ಯುತ್ತದೆ."
                ),
                "difficulty": 1,
            },
            {
                "question_en": "A leaf kept in the dark for two days, then tested with iodine, will…",
                "question_kn": "ಎರಡು ದಿನ ಕತ್ತಲಿನಲ್ಲಿಟ್ಟ ಎಲೆಗೆ ಅಯೋಡಿನ್ ಪರೀಕ್ಷೆ ಮಾಡಿದರೆ ಏನಾಗುತ್ತದೆ?",
                "options_en": [
                    "turn blue-black",
                    "not turn blue-black, because no starch was made",
                    "turn green",
                    "release oxygen",
                ],
                "options_kn": [
                    "ನೀಲಿ-ಕಪ್ಪು ಆಗುತ್ತದೆ",
                    "ನೀಲಿ-ಕಪ್ಪು ಆಗುವುದಿಲ್ಲ; ಏಕೆಂದರೆ ಪಿಷ್ಟ ತಯಾರಾಗಿಲ್ಲ",
                    "ಹಸಿರು ಆಗುತ್ತದೆ",
                    "ಆಮ್ಲಜನಕ ಬಿಡುಗಡೆಯಾಗುತ್ತದೆ",
                ],
                "correct_index": 1,
                "explanation_en": (
                    "Iodine detects starch. Without light the leaf cannot make glucose, so no "
                    "starch is stored and the colour does not change."
                ),
                "explanation_kn": (
                    "ಅಯೋಡಿನ್ ಪಿಷ್ಟವನ್ನು ಪತ್ತೆ ಮಾಡುತ್ತದೆ. ಬೆಳಕಿಲ್ಲದೆ ಎಲೆ "
                    "ಗ್ಲೂಕೋಸ್ ತಯಾರಿಸಲಾರದು; ಆದ್ದರಿಂದ ಪಿಷ್ಟ ಸಂಗ್ರಹವಾಗದೆ "
                    "ಬಣ್ಣ ಬದಲಾಗುವುದಿಲ್ಲ."
                ),
                "difficulty": 3,
            },
            {
                "question_en": "Why do guard cells close the stomata on a hot dry day?",
                "question_kn": "ಬಿಸಿ ಒಣ ದಿನದಲ್ಲಿ ರಕ್ಷಕ ಜೀವಕೋಶಗಳು ಪತ್ರರಂಧ್ರಗಳನ್ನು ಏಕೆ ಮುಚ್ಚುತ್ತವೆ?",
                "options_en": [
                    "to stop photosynthesis completely",
                    "to reduce water loss",
                    "to absorb more carbon dioxide",
                    "to release starch",
                ],
                "options_kn": [
                    "ದ್ಯುತಿಸಂಶ್ಲೇಷಣೆಯನ್ನು ಸಂಪೂರ್ಣ ನಿಲ್ಲಿಸಲು",
                    "ನೀರಿನ ನಷ್ಟವನ್ನು ಕಡಿಮೆ ಮಾಡಲು",
                    "ಹೆಚ್ಚು ಇಂಗಾಲದ ಡೈಆಕ್ಸೈಡ್ ಹೀರಲು",
                    "ಪಿಷ್ಟ ಬಿಡುಗಡೆ ಮಾಡಲು",
                ],
                "correct_index": 1,
                "explanation_en": (
                    "Open stomata also let water vapour escape, so closing them protects the plant "
                    "from drying out even though it slows carbon dioxide intake."
                ),
                "explanation_kn": (
                    "ತೆರೆದ ಪತ್ರರಂಧ್ರಗಳಿಂದ ನೀರಿನ ಆವಿಯೂ ಹೊರಹೋಗುತ್ತದೆ; "
                    "ಅವನ್ನು ಮುಚ್ಚುವುದರಿಂದ ಇಂಗಾಲದ ಡೈಆಕ್ಸೈಡ್ ಸ್ವೀಕಾರ "
                    "ನಿಧಾನವಾದರೂ ಸಸ್ಯ ಒಣಗುವುದನ್ನು ತಡೆಯುತ್ತದೆ."
                ),
                "difficulty": 2,
            },
            {
                "question_en": "Which statement about photosynthesis is correct?",
                "question_kn": "ದ್ಯುತಿಸಂಶ್ಲೇಷಣೆಯ ಬಗ್ಗೆ ಸರಿಯಾದ ಹೇಳಿಕೆ ಯಾವುದು?",
                "options_en": [
                    "It happens only at night",
                    "It needs light and chlorophyll",
                    "It produces carbon dioxide",
                    "It happens only in roots",
                ],
                "options_kn": [
                    "ಇದು ರಾತ್ರಿ ಮಾತ್ರ ನಡೆಯುತ್ತದೆ",
                    "ಇದಕ್ಕೆ ಬೆಳಕು ಮತ್ತು ಕ್ಲೋರೊಫಿಲ್ ಬೇಕು",
                    "ಇದು ಇಂಗಾಲದ ಡೈಆಕ್ಸೈಡ್ ಉತ್ಪಾದಿಸುತ್ತದೆ",
                    "ಇದು ಬೇರುಗಳಲ್ಲಿ ಮಾತ್ರ ನಡೆಯುತ್ತದೆ",
                ],
                "correct_index": 1,
                "explanation_en": (
                    "Light supplies the energy and chlorophyll traps it; without either, the plant "
                    "cannot make glucose."
                ),
                "explanation_kn": (
                    "ಬೆಳಕು ಶಕ್ತಿ ನೀಡುತ್ತದೆ, ಕ್ಲೋರೊಫಿಲ್ ಅದನ್ನು ಹಿಡಿಯುತ್ತದೆ; "
                    "ಎರಡೂ ಇಲ್ಲದಿದ್ದರೆ ಸಸ್ಯ ಗ್ಲೂಕೋಸ್ ತಯಾರಿಸಲಾರದು."
                ),
                "difficulty": 2,
            },
        ],
    },
    {
        "number": 102,
        "category": "enrichment",
        "is_enrichment": True,
        "title_en": "The Human Brain: Control Centre of the Body",
        "title_kn": "ಮಾನವ ಮಿದುಳು: ದೇಹದ ನಿಯಂತ್ರಣ ಕೇಂದ್ರ",
        "summary_en": (
            "Explore an interactive brain diagram: click the cerebrum, cerebellum and brainstem to "
            "learn what each part does."
        ),
        "summary_kn": (
            "ಸಂವಾದಾತ್ಮಕ ಮಿದುಳಿನ ಚಿತ್ರವನ್ನು ಅನ್ವೇಷಿಸಿ: ಸೆರೆಬ್ರಮ್, "
            "ಸೆರೆಬೆಲ್ಲಮ್ ಮತ್ತು ಮಿದುಳುಕಾಂಡವನ್ನು ಕ್ಲಿಕ್ ಮಾಡಿ ಪ್ರತಿಯೊಂದರ "
            "ಕೆಲಸವನ್ನು ತಿಳಿಯಿರಿ."
        ),
        "estimated_minutes": 30,
        "visualizations": ["brain"],
        "topics": [
            {
                "title_en": "Cerebrum: thinking and memory",
                "title_kn": "ಸೆರೆಬ್ರಮ್: ಆಲೋಚನೆ ಮತ್ತು ಸ್ಮೃತಿ",
                "objectives_en": [
                    "Locate the cerebrum and state its main functions.",
                    "Explain what the left and right halves specialise in.",
                ],
                "objectives_kn": [
                    "ಸೆರೆಬ್ರಮ್‌ನ ಸ್ಥಾನ ಮತ್ತು ಮುಖ್ಯ ಕೆಲಸಗಳನ್ನು ತಿಳಿಯುವುದು.",
                    "ಎಡ ಮತ್ತು ಬಲ ಭಾಗಗಳ ವಿಶೇಷ ಕಾರ್ಯಗಳನ್ನು ವಿವರಿಸುವುದು.",
                ],
                "body_en": [
                    "The cerebrum is the largest part of the brain, folded into ridges and grooves "
                    "to pack a large surface into the skull. It is the seat of conscious thought: "
                    "learning, memory, language, imagination, decision-making and voluntary "
                    "movement all happen here.",
                    "The cerebrum is divided into two hemispheres joined by a thick bundle of nerve "
                    "fibres. In most people the left hemisphere handles language and step-by-step "
                    "logic, while the right handles spatial sense, recognising faces and music. The "
                    "outer layer, the cortex, is grey matter where most of this processing happens. "
                    "Different regions along the cortex receive signals from the skin, control "
                    "muscles and interpret what the eyes see.",
                ],
                "body_kn": [
                    "ಸೆರೆಬ್ರಮ್ ಮಿದುಳಿನ ಅತಿ ದೊಡ್ಡ ಭಾಗ; ತಲೆಬುರುಡೆಯಲ್ಲಿ "
                    "ಹೆಚ್ಚು ಮೇಲ್ಮೈಯನ್ನು ಇಡಲು ಅದು ಸುಕ್ಕು ಮತ್ತು ಸಾಲುಗಳಾಗಿ "
                    "ಮಡಚಿಕೊಂಡಿದೆ. ಪ್ರಜ್ಞಾಪೂರ್ವಕ ಆಲೋಚನೆಯ ಕೇಂದ್ರ ಅದು: "
                    "ಕಲಿಕೆ, ಸ್ಮೃತಿ, ಭಾಷೆ, ಕಲ್ಪನೆ, ನಿರ್ಧಾರ ಮತ್ತು ಸ್ವ ಇಚ್ಛೆಯ "
                    "ಚಲನೆ ಎಲ್ಲವೂ ಇಲ್ಲಿ ನಡೆಯುತ್ತವೆ.",
                    "ಸೆರೆಬ್ರಮ್ ದಪ್ಪ ನರ ತಂತುಗಳ ಗುಚ್ಛದಿಂದ ಸೇರಿದ ಎರಡು "
                    "ಅರ್ಧಗೋಳಗಳಾಗಿ ವಿಭಾಗವಾಗಿದೆ. ಬಹುತೇಕ ಜನರಲ್ಲಿ ಎಡ ಅರ್ಧಗೋಳ "
                    "ಭಾಷೆ ಮತ್ತು ಹಂತ ಹಂತದ ತರ್ಕವನ್ನು ನಿರ್ವಹಿಸುತ್ತದೆ; ಬಲ "
                    "ಅರ್ಧಗೋಳ ಪ್ರದೇಶ ಜ್ಞಾನ, ಮುಖ ಗುರುತಿಸುವಿಕೆ ಮತ್ತು ಸಂಗೀತವನ್ನು "
                    "ನಿರ್ವಹಿಸುತ್ತದೆ. ಹೊರ ಪದರವಾದ ಕಾರ್ಟೆಕ್ಸ್ ಬೂದು ದ್ರವ್ಯ; "
                    "ಬಹುತೇಕ ಸಂಸ್ಕರಣೆ ಇಲ್ಲಿ ನಡೆಯುತ್ತದೆ. ಕಾರ್ಟೆಕ್ಸ್‌ನ "
                    "ಬೇರೆ ಬೇರೆ ಭಾಗಗಳು ಚರ್ಮದಿಂದ ಸಂಜ್ಞೆಗಳನ್ನು ಸ್ವೀಕರಿಸಿ, "
                    "ಸ್ನಾಯುಗಳನ್ನು ನಿಯಂತ್ರಿಸಿ, ಕಣ್ಣು ಕಾಣುವುದನ್ನು "
                    "ಅರ್ಥೈಸುತ್ತವೆ.",
                ],
                "key_terms": [
                    {
                        "kn": "ಸೆರೆಬ್ರಮ್",
                        "en": "Cerebrum",
                        "meaning_kn": "ಆಲೋಚನೆ, ಸ್ಮೃತಿ ಮತ್ತು ಸ್ವ ಇಚ್ಛೆಯ ಚಲನೆಯ ಕೇಂದ್ರ.",
                        "meaning_en": "The centre for thought, memory and voluntary movement.",
                    },
                    {
                        "kn": "ಕಾರ್ಟೆಕ್ಸ್",
                        "en": "Cortex",
                        "meaning_kn": "ಸೆರೆಬ್ರಮ್‌ನ ಹೊರ ಪದರ.",
                        "meaning_en": "The outer layer of the cerebrum.",
                    },
                ],
                "example_en": (
                    "When you solve a maths problem, recall a friend's face and then decide to "
                    "raise your hand, all three steps are being handled by your cerebrum."
                ),
                "example_kn": (
                    "ಗಣಿತದ ಸಮಸ್ಯೆ ಬಿಡಿಸುವಾಗ, ಸ್ನೇಹಿತನ ಮುಖ ನೆನಪಿಸಿಕೊಳ್ಳುವಾಗ, "
                    "ನಂತರ ಕೈ ಎತ್ತಲು ನಿರ್ಧರಿಸುವಾಗ — ಈ ಮೂರೂ ಹಂತಗಳನ್ನು ನಿಮ್ಮ "
                    "ಸೆರೆಬ್ರಮ್ ನಿರ್ವಹಿಸುತ್ತದೆ."
                ),
            },
            {
                "title_en": "Cerebellum: balance and smooth movement",
                "title_kn": "ಸೆರೆಬೆಲ್ಲಮ್: ಸಮತೋಲನ ಮತ್ತು ನಯವಾದ ಚಲನೆ",
                "objectives_en": [
                    "Locate the cerebellum and describe its role.",
                    "Explain why cycling becomes easier with practice.",
                ],
                "objectives_kn": [
                    "ಸೆರೆಬೆಲ್ಲಮ್‌ನ ಸ್ಥಾನ ಮತ್ತು ಪಾತ್ರವನ್ನು ವಿವರಿಸುವುದು.",
                    "ಅಭ್ಯಾಸದಿಂದ ಸೈಕಲ್ ಸವಾರಿ ಸುಲಭವಾಗುವುದು ಏಕೆ ಎಂಬುದನ್ನು ವಿವರಿಸುವುದು.",
                ],
                "body_en": [
                    "The cerebellum sits below and behind the cerebrum, at the back of the head. It "
                    "does not decide what to do; it makes sure the movement is accurate, timed and "
                    "balanced. It receives information about body position from the inner ear, "
                    "muscles and joints, and compares it with the movement the cerebrum intended.",
                    "This is why you can walk without watching your feet, and why cycling, "
                    "skating or writing feels clumsy at first and effortless later. The cerebellum "
                    "stores learned movement patterns, so repeated practice turns a conscious "
                    "effort into an automatic skill. It also fine-tunes the muscles that keep you "
                    "upright when you stand still.",
                ],
                "body_kn": [
                    "ಸೆರೆಬೆಲ್ಲಮ್ ಸೆರೆಬ್ರಮ್‌ನ ಕೆಳಗೆ ಮತ್ತು ಹಿಂದೆ, ತಲೆಯ "
                    "ಹಿಂಭಾಗದಲ್ಲಿದೆ. ಏನು ಮಾಡಬೇಕು ಎಂಬುದನ್ನು ಅದು ನಿರ್ಧರಿಸುವುದಿಲ್ಲ; "
                    "ಚಲನೆ ನಿಖರ, ಸಮಯೋಚಿತ ಮತ್ತು ಸಮತೋಲಿತವಾಗಿರುವುದನ್ನು "
                    "ಖಚಿತಪಡಿಸುತ್ತದೆ. ಒಳಗಿನ ಕಿವಿ, ಸ್ನಾಯು ಮತ್ತು ಕೀಲುಗಳಿಂದ "
                    "ದೇಹದ ಸ್ಥಾನದ ಮಾಹಿತಿ ಪಡೆದು, ಸೆರೆಬ್ರಮ್ ಉದ್ದೇಶಿಸಿದ "
                    "ಚಲನೆಯೊಂದಿಗೆ ಹೋಲಿಸುತ್ತದೆ.",
                    "ಆದ್ದರಿಂದ ನಿಮ್ಮ ಕಾಲುಗಳನ್ನು ನೋಡದೆಯೂ ನಡೆಯಬಹುದು; "
                    "ಮೊದಲಿಗೆ ಸೈಕಲ್ ಸವಾರಿ, ಸ್ಕೇಟಿಂಗ್ ಅಥವಾ ಬರವಣಿಗೆ "
                    "ಒಡ್ಡೊಡ್ಡಾಗಿ ಕಾಣುತ್ತದೆ, ನಂತರ ಸುಲಭವಾಗುತ್ತದೆ. "
                    "ಸೆರೆಬೆಲ್ಲಮ್ ಕಲಿತ ಚಲನೆಯ ಮಾದರಿಗಳನ್ನು ಸಂಗ್ರಹಿಸುತ್ತದೆ; "
                    "ಪುನರಾವರ್ತಿತ ಅಭ್ಯಾಸ ಪ್ರಜ್ಞಾಪೂರ್ವಕ ಪ್ರಯತ್ನವನ್ನು "
                    "ಸ್ವಯಂಚಾಲಿತ ಕೌಶಲ್ಯವಾಗಿ ಬದಲಿಸುತ್ತದೆ. ನಿಶ್ಚಲವಾಗಿ "
                    "ನಿಂತಾಗ ನೇರವಾಗಿ ಇರಿಸುವ ಸ್ನಾಯುಗಳನ್ನೂ ಅದು ಸೂಕ್ಷ್ಮವಾಗಿ "
                    "ನಿಯಂತ್ರಿಸುತ್ತದೆ.",
                ],
                "key_terms": [
                    {
                        "kn": "ಸೆರೆಬೆಲ್ಲಮ್",
                        "en": "Cerebellum",
                        "meaning_kn": "ಸಮತೋಲನ ಮತ್ತು ನಯವಾದ ಚಲನೆಯನ್ನು ನಿಯಂತ್ರಿಸುವ ಭಾಗ.",
                        "meaning_en": "The part that controls balance and smooth movement.",
                    },
                    {
                        "kn": "ಸ್ವಯಂಚಾಲಿತ ಕೌಶಲ್ಯ",
                        "en": "Automatic skill",
                        "meaning_kn": "ಅಭ್ಯಾಸದಿಂದ ಆಲೋಚನೆ ಇಲ್ಲದೆ ಮಾಡಬಹುದಾದ ಕೆಲಸ.",
                        "meaning_en": "A skill performed without conscious effort after practice.",
                    },
                ],
                "example_en": (
                    "A cricketer who has practised catching for years does not calculate the ball's "
                    "path: the cerebellum has stored the pattern and adjusts the hands instantly."
                ),
                "example_kn": (
                    "ವರ್ಷಗಳಿಂದ ಕ್ಯಾಚ್ ಅಭ್ಯಾಸ ಮಾಡಿದ ಕ್ರಿಕೆಟಿಗ ಚೆಂಡಿನ "
                    "ಮಾರ್ಗವನ್ನು ಲೆಕ್ಕ ಹಾಕುವುದಿಲ್ಲ: ಸೆರೆಬೆಲ್ಲಮ್ ಆ ಮಾದರಿಯನ್ನು "
                    "ಸಂಗ್ರಹಿಸಿ ಕೈಗಳನ್ನು ಕ್ಷಣಮಾತ್ರದಲ್ಲಿ ಹೊಂದಿಸುತ್ತದೆ."
                ),
            },
            {
                "title_en": "Brainstem: the body's automatic pilot",
                "title_kn": "ಮಿದುಳುಕಾಂಡ: ದೇಹದ ಸ್ವಯಂಚಾಲಿತ ನಿಯಂತ್ರಕ",
                "objectives_en": [
                    "Describe the functions of the brainstem.",
                    "Explain why breathing continues during sleep.",
                ],
                "objectives_kn": [
                    "ಮಿದುಳುಕಾಂಡದ ಕಾರ್ಯಗಳನ್ನು ವಿವರಿಸುವುದು.",
                    "ನಿದ್ರೆಯಲ್ಲೂ ಉಸಿರಾಟ ಮುಂದುವರಿಯುವುದು ಏಕೆ ಎಂಬುದನ್ನು ವಿವರಿಸುವುದು.",
                ],
                "body_en": [
                    "The brainstem is the stalk that joins the brain to the spinal cord. It "
                    "controls the functions you never think about: breathing, heart rate, blood "
                    "pressure, swallowing, coughing and the sleep-wake cycle. Because these "
                    "controls sit here rather than in the cerebrum, breathing continues while you "
                    "are asleep or unconscious.",
                    "The brainstem also acts as a gateway. Nearly every signal travelling between "
                    "the brain and the body passes through it, and it sorts these signals on the "
                    "way. Its lower part, the medulla, is where nerves cross over, which is why the "
                    "left side of the brain controls the right side of the body. Injury here is "
                    "especially serious because so many vital controls are gathered in a small "
                    "space.",
                ],
                "body_kn": [
                    "ಮಿದುಳುಕಾಂಡ ಮಿದುಳನ್ನು ಬೆನ್ನುಹುರಿಗೆ ಜೋಡಿಸುವ ಕಾಂಡ. "
                    "ನೀವು ಎಂದೂ ಯೋಚಿಸದ ಕಾರ್ಯಗಳನ್ನು ಅದು ನಿಯಂತ್ರಿಸುತ್ತದೆ: "
                    "ಉಸಿರಾಟ, ಹೃದಯ ಬಡಿತ, ರಕ್ತದೊತ್ತಡ, ನುಂಗುವಿಕೆ, ಕೆಮ್ಮು ಮತ್ತು "
                    "ನಿದ್ರೆ-ಎಚ್ಚರ ಚಕ್ರ. ಈ ನಿಯಂತ್ರಣಗಳು ಸೆರೆಬ್ರಮ್‌ನಲ್ಲದೆ "
                    "ಇಲ್ಲಿ ಇರುವುದರಿಂದ ನೀವು ನಿದ್ರಿಸುತ್ತಿರುವಾಗ ಅಥವಾ "
                    "ಪ್ರಜ್ಞೆ ತಪ್ಪಿದಾಗಲೂ ಉಸಿರಾಟ ಮುಂದುವರಿಯುತ್ತದೆ.",
                    "ಮಿದುಳುಕಾಂಡ ಪ್ರವೇಶದ್ವಾರವೂ ಹೌದು. ಮಿದುಳು ಮತ್ತು ದೇಹದ "
                    "ನಡುವೆ ಸಾಗುವ ಬಹುತೇಕ ಎಲ್ಲಾ ಸಂಜ್ಞೆಗಳು ಇದರ ಮೂಲಕ "
                    "ಹಾದುಹೋಗುತ್ತವೆ; ಅವನ್ನು ಇದು ವಿಂಗಡಿಸುತ್ತದೆ. ಇದರ ಕೆಳ "
                    "ಭಾಗವಾದ ಮೆಡುಲ್ಲಾದಲ್ಲಿ ನರಗಳು ಅಡ್ಡಹಾಯುತ್ತವೆ; ಆದ್ದರಿಂದ "
                    "ಮಿದುಳಿನ ಎಡ ಭಾಗ ದೇಹದ ಬಲ ಭಾಗವನ್ನು ನಿಯಂತ್ರಿಸುತ್ತದೆ. "
                    "ಇಲ್ಲಿ ಗಾಯವಾದರೆ ಬಹಳ ಗಂಭೀರ; ಏಕೆಂದರೆ ಅನೇಕ ಪ್ರಾಣ "
                    "ನಿಯಂತ್ರಣಗಳು ಸಣ್ಣ ಜಾಗದಲ್ಲಿ ಸೇರಿವೆ.",
                ],
                "key_terms": [
                    {
                        "kn": "ಮಿದುಳುಕಾಂಡ",
                        "en": "Brainstem",
                        "meaning_kn": "ಉಸಿರಾಟ, ಹೃದಯ ಬಡಿತದಂತಹ ಸ್ವಯಂಚಾಲಿತ ಕಾರ್ಯಗಳ ನಿಯಂತ್ರಕ.",
                        "meaning_en": "The controller of automatic functions such as breathing.",
                    },
                    {
                        "kn": "ಮೆಡುಲ್ಲಾ",
                        "en": "Medulla",
                        "meaning_kn": "ಮಿದುಳುಕಾಂಡದ ಕೆಳ ಭಾಗ; ನರಗಳು ಇಲ್ಲಿ ಅಡ್ಡಹಾಯುತ್ತವೆ.",
                        "meaning_en": "The lower brainstem, where nerves cross over.",
                    },
                ],
                "example_en": (
                    "You do not wake up to remind yourself to breathe: the brainstem keeps the "
                    "rhythm going all night without any conscious instruction."
                ),
                "example_kn": (
                    "ಉಸಿರಾಡಲು ನೆನಪಿಸಲು ನೀವು ರಾತ್ರಿ ಎಚ್ಚರಗೊಳ್ಳುವುದಿಲ್ಲ: "
                    "ಮಿದುಳುಕಾಂಡ ಪ್ರಜ್ಞಾಪೂರ್ವಕ ಸೂಚನೆ ಇಲ್ಲದೆಯೇ ರಾತ್ರಿಯೆಲ್ಲಾ "
                    "ಲಯವನ್ನು ಮುಂದುವರಿಸುತ್ತದೆ."
                ),
            },
        ],
        "notes_en": [
            "Cerebrum: largest part; thinking, memory, language, voluntary movement.",
            "Cerebellum: balance, posture and smooth, practised movement.",
            "Brainstem: breathing, heart rate, blood pressure, swallowing, sleep-wake cycle.",
            "The brainstem is the gateway for signals between brain and body.",
            "Nerves cross in the medulla, so the left brain controls the right side.",
            "Practice moves skills from conscious control towards automatic control.",
        ],
        "notes_kn": [
            "ಸೆರೆಬ್ರಮ್: ಅತಿ ದೊಡ್ಡ ಭಾಗ; ಆಲೋಚನೆ, ಸ್ಮೃತಿ, ಭಾಷೆ, ಸ್ವ ಇಚ್ಛೆಯ ಚಲನೆ.",
            "ಸೆರೆಬೆಲ್ಲಮ್: ಸಮತೋಲನ, ನಿಲುವು ಮತ್ತು ನಯವಾದ ಅಭ್ಯಾಸದ ಚಲನೆ.",
            "ಮಿದುಳುಕಾಂಡ: ಉಸಿರಾಟ, ಹೃದಯ ಬಡಿತ, ರಕ್ತದೊತ್ತಡ, ನುಂಗುವಿಕೆ, ನಿದ್ರೆ-ಎಚ್ಚರ ಚಕ್ರ.",
            "ಮಿದುಳು ಮತ್ತು ದೇಹದ ನಡುವಿನ ಸಂಜ್ಞೆಗಳಿಗೆ ಮಿದುಳುಕಾಂಡ ಪ್ರವೇಶದ್ವಾರ.",
            "ಮೆಡುಲ್ಲಾದಲ್ಲಿ ನರಗಳು ಅಡ್ಡಹಾಯುತ್ತವೆ; ಆದ್ದರಿಂದ ಎಡ ಮಿದುಳು ಬಲ ಭಾಗವನ್ನು ನಿಯಂತ್ರಿಸುತ್ತದೆ.",
            "ಅಭ್ಯಾಸ ಕೌಶಲ್ಯವನ್ನು ಪ್ರಜ್ಞಾಪೂರ್ವಕ ನಿಯಂತ್ರಣದಿಂದ ಸ್ವಯಂಚಾಲಿತ ನಿಯಂತ್ರಣಕ್ಕೆ ಒಯ್ಯುತ್ತದೆ.",
        ],
        "videos": [
            {
                "title": "ಮಾನವ ಮಿದುಳು — ಕನ್ನಡ",
                "language": "kn",
                "topic": "Human brain",
                "search_query": "ಮಾನವ ಮಿದುಳು ಕನ್ನಡ 8ನೇ ತರಗತಿ ವಿಜ್ಞಾನ ಭಾಗಗಳು ಕಾರ್ಯ",
            },
            {
                "title": "Human brain parts and functions",
                "language": "en",
                "topic": "Human brain",
                "search_query": "human brain cerebrum cerebellum brainstem class 8 functions",
            },
        ],
        "quiz": [
            {
                "question_en": "Which part of the brain controls balance and coordination?",
                "question_kn": "ಮಿದುಳಿನ ಯಾವ ಭಾಗ ಸಮತೋಲನ ಮತ್ತು ಸಮನ್ವಯವನ್ನು ನಿಯಂತ್ರಿಸುತ್ತದೆ?",
                "options_en": ["Cerebrum", "Cerebellum", "Medulla", "Spinal cord"],
                "options_kn": ["ಸೆರೆಬ್ರಮ್", "ಸೆರೆಬೆಲ್ಲಮ್", "ಮೆಡುಲ್ಲಾ", "ಬೆನ್ನುಹುರಿ"],
                "correct_index": 1,
                "explanation_en": (
                    "The cerebellum fine-tunes posture and makes practised movements smooth and "
                    "balanced."
                ),
                "explanation_kn": (
                    "ಸೆರೆಬೆಲ್ಲಮ್ ನಿಲುವನ್ನು ಸೂಕ್ಷ್ಮವಾಗಿ ಹೊಂದಿಸಿ ಅಭ್ಯಾಸದ "
                    "ಚಲನೆಗಳನ್ನು ನಯವಾಗಿ, ಸಮತೋಲಿತವಾಗಿ ಮಾಡುತ್ತದೆ."
                ),
                "difficulty": 1,
            },
            {
                "question_en": "Breathing continues during sleep because it is controlled by the…",
                "question_kn": "ನಿದ್ರೆಯಲ್ಲೂ ಉಸಿರಾಟ ಮುಂದುವರಿಯುವುದು ಯಾಕೆ? ಅದನ್ನು ನಿಯಂತ್ರಿಸುವುದು…",
                "options_en": ["cerebrum", "cerebellum", "brainstem", "eyes"],
                "options_kn": ["ಸೆರೆಬ್ರಮ್", "ಸೆರೆಬೆಲ್ಲಮ್", "ಮಿದುಳುಕಾಂಡ", "ಕಣ್ಣುಗಳು"],
                "correct_index": 2,
                "explanation_en": (
                    "The brainstem controls automatic functions like breathing and heart rate, so "
                    "they do not depend on conscious thought."
                ),
                "explanation_kn": (
                    "ಮಿದುಳುಕಾಂಡ ಉಸಿರಾಟ ಮತ್ತು ಹೃದಯ ಬಡಿತದಂತಹ ಸ್ವಯಂಚಾಲಿತ "
                    "ಕಾರ್ಯಗಳನ್ನು ನಿಯಂತ್ರಿಸುತ್ತದೆ; ಅವು ಪ್ರಜ್ಞಾಪೂರ್ವಕ "
                    "ಆಲೋಚನೆಯನ್ನು ಅವಲಂಬಿಸುವುದಿಲ್ಲ."
                ),
                "difficulty": 1,
            },
            {
                "question_en": "Remembering a poem for an exam is mainly a function of the…",
                "question_kn": "ಪರೀಕ್ಷೆಗಾಗಿ ಪದ್ಯ ನೆನಪಿಟ್ಟುಕೊಳ್ಳುವುದು ಮುಖ್ಯವಾಗಿ ಯಾವ ಭಾಗದ ಕೆಲಸ?",
                "options_en": ["cerebrum", "cerebellum", "medulla", "spinal cord"],
                "options_kn": ["ಸೆರೆಬ್ರಮ್", "ಸೆರೆಬೆಲ್ಲಮ್", "ಮೆಡುಲ್ಲಾ", "ಬೆನ್ನುಹುರಿ"],
                "correct_index": 0,
                "explanation_en": (
                    "Memory and language are cerebrum functions; the cerebellum stores movement "
                    "patterns, not poems."
                ),
                "explanation_kn": (
                    "ಸ್ಮೃತಿ ಮತ್ತು ಭಾಷೆ ಸೆರೆಬ್ರಮ್‌ನ ಕಾರ್ಯಗಳು; ಸೆರೆಬೆಲ್ಲಮ್ "
                    "ಚಲನೆಯ ಮಾದರಿಗಳನ್ನು ಸಂಗ್ರಹಿಸುತ್ತದೆ, ಪದ್ಯಗಳನ್ನು ಅಲ್ಲ."
                ),
                "difficulty": 2,
            },
            {
                "question_en": "Why does the left side of the brain control the right side of the body?",
                "question_kn": "ಮಿದುಳಿನ ಎಡ ಭಾಗ ದೇಹದ ಬಲ ಭಾಗವನ್ನು ಏಕೆ ನಿಯಂತ್ರಿಸುತ್ತದೆ?",
                "options_en": [
                    "Because the body is symmetrical",
                    "Because nerves cross over in the medulla",
                    "Because the cerebrum is on the right",
                    "Because muscles pull only one way",
                ],
                "options_kn": [
                    "ದೇಹ ಸಮಮಿತಿಯಲ್ಲಿರುವುದರಿಂದ",
                    "ಮೆಡುಲ್ಲಾದಲ್ಲಿ ನರಗಳು ಅಡ್ಡಹಾಯುವುದರಿಂದ",
                    "ಸೆರೆಬ್ರಮ್ ಬಲಭಾಗದಲ್ಲಿರುವುದರಿಂದ",
                    "ಸ್ನಾಯುಗಳು ಒಂದೇ ದಿಕ್ಕಿಗೆ ಎಳೆಯುವುದರಿಂದ",
                ],
                "correct_index": 1,
                "explanation_en": (
                    "Motor fibres cross to the opposite side in the lower brainstem, so each "
                    "hemisphere controls the opposite half of the body."
                ),
                "explanation_kn": (
                    "ಚಲನೆಯ ನರತಂತುಗಳು ಕೆಳ ಮಿದುಳುಕಾಂಡದಲ್ಲಿ ಎದುರು ಭಾಗಕ್ಕೆ "
                    "ಅಡ್ಡಹಾಯುತ್ತವೆ; ಆದ್ದರಿಂದ ಪ್ರತಿ ಅರ್ಧಗೋಳವೂ ದೇಹದ "
                    "ಎದುರು ಅರ್ಧವನ್ನು ನಿಯಂತ್ರಿಸುತ್ತದೆ."
                ),
                "difficulty": 3,
            },
            {
                "question_en": "Which list contains only brainstem functions?",
                "question_kn": "ಯಾವ ಪಟ್ಟಿಯಲ್ಲಿ ಮಿದುಳುಕಾಂಡದ ಕಾರ್ಯಗಳು ಮಾತ್ರ ಇವೆ?",
                "options_en": [
                    "Heart rate, breathing, blood pressure",
                    "Solving puzzles, writing poetry",
                    "Balancing on one leg, catching a ball",
                    "Seeing colours, hearing music",
                ],
                "options_kn": [
                    "ಹೃದಯ ಬಡಿತ, ಉಸಿರಾಟ, ರಕ್ತದೊತ್ತಡ",
                    "ಒಗಟು ಬಿಡಿಸುವುದು, ಕವನ ಬರೆಯುವುದು",
                    "ಒಂದು ಕಾಲಿನ ಮೇಲೆ ನಿಲ್ಲುವುದು, ಚೆಂಡು ಹಿಡಿಯುವುದು",
                    "ಬಣ್ಣ ನೋಡುವುದು, ಸಂಗೀತ ಕೇಳುವುದು",
                ],
                "correct_index": 0,
                "explanation_en": (
                    "Heart rate, breathing and blood pressure are automatic controls of the "
                    "brainstem. The other options involve the cerebrum or cerebellum."
                ),
                "explanation_kn": (
                    "ಹೃದಯ ಬಡಿತ, ಉಸಿರಾಟ ಮತ್ತು ರಕ್ತದೊತ್ತಡ ಮಿದುಳುಕಾಂಡದ "
                    "ಸ್ವಯಂಚಾಲಿತ ನಿಯಂತ್ರಣಗಳು. ಉಳಿದವು ಸೆರೆಬ್ರಮ್ ಅಥವಾ "
                    "ಸೆರೆಬೆಲ್ಲಮ್‌ಗೆ ಸಂಬಂಧಿಸಿವೆ."
                ),
                "difficulty": 2,
            },
        ],
    },
)
