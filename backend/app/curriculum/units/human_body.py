"""Human body and organ systems: an illustrated biology learning unit.

This unit is *enrichment*: the Karnataka Class 8 course list supplied for this project does not
contain a separate human-body unit, so the interface labels it as supplementary. Every sentence
below is original WonderNest writing, and the anatomy is kept to the level a Class 8 student
needs: what each organ does, how the parts fit together, and how to remember it.
"""

UNITS: tuple[dict, ...] = (
    {
        "number": 103,
        "category": "biology",
        "is_enrichment": True,
        "title_en": "Human Body and Organ Systems",
        "title_kn": "ಮಾನವ ದೇಹ ಮತ್ತು ಅಂಗ ವ್ಯವಸ್ಥೆಗಳು",
        "summary_en": (
            "Meet the control centre, the pump and the delivery network inside you: the brain, "
            "the heart, the circulatory system, the nervous system and the blood that links them."
        ),
        "summary_kn": (
            "ನಿಮ್ಮ ಒಳಗಿನ ನಿಯಂತ್ರಣ ಕೇಂದ್ರ, ಪಂಪ್ ಮತ್ತು ಸಾಗಣೆ ಜಾಲವನ್ನು ತಿಳಿಯಿರಿ: "
            "ಮಿದುಳು, ಹೃದಯ, ರಕ್ತಪರಿಚಲನಾ ವ್ಯವಸ್ಥೆ, ನರಮಂಡಲ ಮತ್ತು ಅವನ್ನು ಬೆಸೆಯುವ ರಕ್ತ."
        ),
        "estimated_minutes": 45,
        "visualizations": ["brain", "heart"],
        "topics": [
            {
                "title_en": "The human brain: your control centre",
                "title_kn": "ಮಾನವ ಮಿದುಳು: ನಿಮ್ಮ ನಿಯಂತ್ರಣ ಕೇಂದ್ರ",
                "objectives_en": [
                    "Name the three main parts of the brain and one job of each.",
                    "Explain how the brain is protected inside the skull.",
                    "Describe why reflex actions happen faster than deliberate actions.",
                ],
                "objectives_kn": [
                    "ಮಿದುಳಿನ ಮೂರು ಮುಖ್ಯ ಭಾಗಗಳನ್ನು ಹೆಸರಿಸಿ ಪ್ರತಿಯೊಂದರ ಒಂದು ಕೆಲಸ ತಿಳಿಸುವುದು.",
                    "ತಲೆಬುರುಡೆಯೊಳಗೆ ಮಿದುಳು ಹೇಗೆ ರಕ್ಷಿಸಲ್ಪಡುತ್ತದೆ ಎಂದು ವಿವರಿಸುವುದು.",
                    "ಪ್ರತಿವರ್ತನ ಕ್ರಿಯೆಗಳು ಉದ್ದೇಶಪೂರ್ವಕ ಕ್ರಿಯೆಗಳಿಗಿಂತ ವೇಗವಾಗಿರುವುದೇಕೆ ಎಂದು ತಿಳಿಸುವುದು.",
                ],
                "body_en": [
                    "Your brain is a soft, folded organ of about 1.3 kilograms that sits inside the "
                    "skull. It receives signals from your senses, compares them with memories, and "
                    "sends instructions to muscles and glands. Three parts do most of the everyday "
                    "work: the cerebrum, the cerebellum and the brainstem.",
                    "The cerebrum is the large, deeply folded upper part. Its outer layer handles "
                    "thinking, memory, language and the interpretation of what you see and hear. "
                    "The cerebellum lies below and behind it and keeps movements smooth and "
                    "balanced, which is why you can cycle without thinking about each muscle. The "
                    "brainstem is the stalk that joins the brain to the spinal cord; it runs "
                    "automatic jobs such as breathing, heartbeat and blood pressure, so it works "
                    "even while you sleep.",
                    "The brain is protected in three layers: the bony skull, three thin membranes "
                    "called meninges, and a fluid cushion called cerebrospinal fluid that floats "
                    "the brain and absorbs shocks. Nerve cells called neurons carry electrical "
                    "signals at great speed, and they do not work well without oxygen and glucose, "
                    "which is why a blow to the head needs medical attention.",
                ],
                "body_kn": [
                    "ನಿಮ್ಮ ಮಿದುಳು ಸುಮಾರು 1.3 ಕಿಲೋಗ್ರಾಂ ತೂಕದ ಮೃದುವಾದ, ಮಡಿಕೆಗಳಿರುವ "
                    "ಅಂಗ; ಇದು ತಲೆಬುರುಡೆಯೊಳಗೆ ಇರುತ್ತದೆ. ಇದು ಇಂದ್ರಿಯಗಳಿಂದ ಸಂಕೇತಗಳನ್ನು "
                    "ಸ್ವೀಕರಿಸಿ, ನೆನಪುಗಳೊಂದಿಗೆ ಹೋಲಿಸಿ, ಸ್ನಾಯು ಮತ್ತು ಗ್ರಂಥಿಗಳಿಗೆ ಸೂಚನೆ "
                    "ಕಳುಹಿಸುತ್ತದೆ. ದಿನನಿತ್ಯದ ಹೆಚ್ಚಿನ ಕೆಲಸವನ್ನು ಮೂರು ಭಾಗಗಳು "
                    "ನಿರ್ವಹಿಸುತ್ತವೆ: ಸೆರೆಬ್ರಮ್, ಸೆರೆಬೆಲ್ಲಮ್ ಮತ್ತು ಮಿದುಳು ಕಾಂಡ.",
                    "ಸೆರೆಬ್ರಮ್ ಎಂಬುದು ದೊಡ್ಡ, ಆಳವಾಗಿ ಮಡಿಕೆ ಬಿದ್ದ ಮೇಲ್ಭಾಗ. ಇದರ ಹೊರ ಪದರ "
                    "ಯೋಚನೆ, ನೆನಪು, ಭಾಷೆ ಮತ್ತು ನೋಡುವ ಹಾಗೂ ಕೇಳುವ ವಿಷಯಗಳ ಅರ್ಥೈಸುವಿಕೆಯನ್ನು "
                    "ನೋಡಿಕೊಳ್ಳುತ್ತದೆ. ಸೆರೆಬೆಲ್ಲಮ್ ಇದರ ಕೆಳಗೆ ಮತ್ತು ಹಿಂದೆ ಇದ್ದು ಚಲನೆಯನ್ನು "
                    "ನಯವಾಗಿಸಿ ಸಮತೋಲನ ಕಾಪಾಡುತ್ತದೆ; ಆದ್ದರಿಂದಲೇ ಪ್ರತಿ ಸ್ನಾಯುವಿನ ಬಗ್ಗೆ "
                    "ಯೋಚಿಸದೆಯೂ ಸೈಕಲ್ ಸವಾರಿ ಮಾಡಲು ಸಾಧ್ಯ. ಮಿದುಳು ಕಾಂಡವು ಮಿದುಳನ್ನು "
                    "ಬೆನ್ನುಹುರಿಗೆ ಜೋಡಿಸುವ ಕಾಂಡ; ಉಸಿರಾಟ, ಹೃದಯಬಡಿತ ಮತ್ತು ರಕ್ತದ ಒತ್ತಡದಂತಹ "
                    "ಸ್ವಯಂಚಾಲಿತ ಕೆಲಸಗಳನ್ನು ನಡೆಸುತ್ತದೆ; ಹಾಗಾಗಿ ನೀವು ನಿದ್ರಿಸುವಾಗಲೂ ಇದು "
                    "ಕೆಲಸ ಮಾಡುತ್ತದೆ.",
                    "ಮಿದುಳು ಮೂರು ಪದರಗಳಿಂದ ರಕ್ಷಿಸಲ್ಪಡುತ್ತದೆ: ಮೂಳೆಯ ತಲೆಬುರುಡೆ, ಮೆನಿಂಜಸ್ "
                    "ಎಂಬ ಮೂರು ತೆಳು ಪೊರೆಗಳು, ಮತ್ತು ಮಿದುಳನ್ನು ತೇಲಿಸಿ ಆಘಾತ ಹೀರಿಕೊಳ್ಳುವ "
                    "ಮಿದುಳು ಬೆನ್ನುಹುರಿ ದ್ರವ. ನ್ಯೂರಾನ್ ಎಂಬ ನರಕಣಗಳು ಅತಿ ವೇಗವಾಗಿ "
                    "ವಿದ್ಯುತ್ ಸಂಕೇತ ಸಾಗಿಸುತ್ತವೆ; ಆಮ್ಲಜನಕ ಮತ್ತು ಗ್ಲೂಕೋಸ್ ಇಲ್ಲದೆ ಅವು "
                    "ಸರಿಯಾಗಿ ಕೆಲಸ ಮಾಡುವುದಿಲ್ಲ; ಆದ್ದರಿಂದ ತಲೆಗೆ ಪೆಟ್ಟಾದರೆ ವೈದ್ಯಕೀಯ "
                    "ಸಹಾಯ ಅಗತ್ಯ.",
                ],
                "key_terms": [
                    {
                        "kn": "ಸೆರೆಬ್ರಮ್",
                        "en": "Cerebrum",
                        "meaning_kn": "ಯೋಚನೆ, ನೆನಪು, ಭಾಷೆ ಮತ್ತು ಇಂದ್ರಿಯಗಳನ್ನು ನೋಡಿಕೊಳ್ಳುವ ಮಿದುಳಿನ ದೊಡ್ಡ ಭಾಗ.",
                        "meaning_en": "The large upper part of the brain that handles thinking, memory, language and the senses.",
                    },
                    {
                        "kn": "ಸೆರೆಬೆಲ್ಲಮ್",
                        "en": "Cerebellum",
                        "meaning_kn": "ಸಮತೋಲನ ಮತ್ತು ನಯವಾದ ಚಲನೆಯನ್ನು ನಿಯಂತ್ರಿಸುವ ಭಾಗ.",
                        "meaning_en": "The part that keeps balance and makes movements smooth and coordinated.",
                    },
                    {
                        "kn": "ಮಿದುಳು ಕಾಂಡ",
                        "en": "Brainstem",
                        "meaning_kn": "ಮಿದುಳನ್ನು ಬೆನ್ನುಹುರಿಗೆ ಜೋಡಿಸಿ ಉಸಿರಾಟ ಮತ್ತು ಹೃದಯಬಡಿತವನ್ನು ನಡೆಸುವ ಭಾಗ.",
                        "meaning_en": "The stalk joining brain to spinal cord that controls breathing and heartbeat.",
                    },
                ],
                "example_en": (
                    "When you catch a ball, your eyes send signals to the cerebrum, which predicts "
                    "where the ball will be; the cerebellum then times your arm muscles so the hand "
                    "arrives at the right moment."
                ),
                "example_kn": (
                    "ನೀವು ಚೆಂಡನ್ನು ಹಿಡಿಯುವಾಗ ಕಣ್ಣುಗಳು ಸೆರೆಬ್ರಮ್‌ಗೆ ಸಂಕೇತ ಕಳುಹಿಸುತ್ತವೆ; "
                    "ಅದು ಚೆಂಡು ಎಲ್ಲಿ ಬರುತ್ತದೆ ಎಂದು ಊಹಿಸುತ್ತದೆ. ನಂತರ ಸೆರೆಬೆಲ್ಲಮ್ ಕೈ "
                    "ಸ್ನಾಯುಗಳ ಸಮಯವನ್ನು ಹೊಂದಿಸಿ ಸರಿಯಾದ ಕ್ಷಣಕ್ಕೆ ಕೈ ಬರುವಂತೆ ಮಾಡುತ್ತದೆ."
                ),
            },
            {
                "title_en": "The human heart: a four-chambered pump",
                "title_kn": "ಮಾನವ ಹೃದಯ: ನಾಲ್ಕು ಕೋಣೆಗಳ ಪಂಪ್",
                "objectives_en": [
                    "Identify the four chambers of the heart and the main vessels attached to it.",
                    "Explain why the left ventricle has a thicker wall than the right.",
                    "Describe the job of valves in the heart.",
                ],
                "objectives_kn": [
                    "ಹೃದಯದ ನಾಲ್ಕು ಕೋಣೆಗಳನ್ನು ಮತ್ತು ಅದಕ್ಕೆ ಜೋಡಣೆಯಾಗಿರುವ ಮುಖ್ಯ ರಕ್ತನಾಳಗಳನ್ನು ಗುರುತಿಸುವುದು.",
                    "ಬಲ ಹೃತ್ಕುಕ್ಷಿಗಿಂತ ಎಡ ಹೃತ್ಕುಕ್ಷಿಯ ಗೋಡೆ ದಪ್ಪವಾಗಿರುವುದೇಕೆ ಎಂದು ವಿವರಿಸುವುದು.",
                    "ಹೃದಯದ ಕವಾಟಗಳ ಕೆಲಸವನ್ನು ವಿವರಿಸುವುದು.",
                ],
                "body_en": [
                    "The heart is a strong muscle about the size of your closed fist, sitting "
                    "slightly left of the middle of your chest. It has four chambers: two small "
                    "atria on top that receive blood, and two larger ventricles below that pump it "
                    "out. The right side of the heart deals with oxygen-poor blood going to the "
                    "lungs, and the left side deals with oxygen-rich blood going to the body.",
                    "Blood enters the right atrium through the vena cava and leaves the right "
                    "ventricle through the pulmonary artery. Oxygen-rich blood returns to the left "
                    "atrium through the pulmonary veins and is pushed out of the left ventricle "
                    "into the aorta, the largest artery in the body. Valves between the chambers "
                    "and at the exits close after each push, so blood can only move forward.",
                    "The left ventricle has the thickest wall because it must push blood through "
                    "the whole body, which is a long path with more resistance than the short trip "
                    "to the lungs. The two sides beat together: the atria contract first to fill "
                    "the ventricles, and then the ventricles contract to send blood out.",
                ],
                "body_kn": [
                    "ಹೃದಯವು ನಿಮ್ಮ ಮುಷ್ಟಿಯ ಗಾತ್ರದ ಬಲವಾದ ಸ್ನಾಯು; ಎದೆಯ ಮಧ್ಯದಿಂದ ಸ್ವಲ್ಪ "
                    "ಎಡಕ್ಕೆ ಇರುತ್ತದೆ. ಇದಕ್ಕೆ ನಾಲ್ಕು ಕೋಣೆಗಳಿವೆ: ಮೇಲೆ ರಕ್ತವನ್ನು "
                    "ಸ್ವೀಕರಿಸುವ ಎರಡು ಸಣ್ಣ ಹೃತ್ಕರ್ಣಗಳು, ಕೆಳಗೆ ಅದನ್ನು ಪಂಪ್ ಮಾಡುವ ಎರಡು "
                    "ದೊಡ್ಡ ಹೃತ್ಕುಕ್ಷಿಗಳು. ಹೃದಯದ ಬಲ ಭಾಗ ಆಮ್ಲಜನಕ ಕಡಿಮೆ ಇರುವ ರಕ್ತವನ್ನು "
                    "ಶ್ವಾಸಕೋಶಕ್ಕೆ ಕಳುಹಿಸುತ್ತದೆ; ಎಡ ಭಾಗ ಆಮ್ಲಜನಕಯುಕ್ತ ರಕ್ತವನ್ನು ದೇಹಕ್ಕೆ "
                    "ಕಳುಹಿಸುತ್ತದೆ.",
                    "ರಕ್ತವು ಮಹಾ ಅಭಿಧಮನಿಯ ಮೂಲಕ ಬಲ ಹೃತ್ಕರ್ಣವನ್ನು ಸೇರಿ, ಬಲ ಹೃತ್ಕುಕ್ಷಿಯಿಂದ "
                    "ಶ್ವಾಸಕೋಶೀಯ ಅಪಧಮನಿಯ ಮೂಲಕ ಹೊರಡುತ್ತದೆ. ಆಮ್ಲಜನಕಯುಕ್ತ ರಕ್ತ "
                    "ಶ್ವಾಸಕೋಶೀಯ ಅಭಿಧಮನಿಗಳ ಮೂಲಕ ಎಡ ಹೃತ್ಕರ್ಣಕ್ಕೆ ಬಂದು, ಎಡ ಹೃತ್ಕುಕ್ಷಿಯಿಂದ "
                    "ದೇಹದ ಅತಿ ದೊಡ್ಡ ಅಪಧಮನಿಯಾದ ಮಹಾಪಧಮನಿಗೆ ಹೋಗುತ್ತದೆ. ಕೋಣೆಗಳ ನಡುವೆ ಮತ್ತು "
                    "ಹೊರದ್ವಾರಗಳಲ್ಲಿ ಇರುವ ಕವಾಟಗಳು ಪ್ರತಿ ಸಂಕೋಚನದ ನಂತರ ಮುಚ್ಚಿಕೊಂಡು ರಕ್ತ "
                    "ಮುಂದಕ್ಕೆ ಮಾತ್ರ ಹರಿಯುವಂತೆ ಮಾಡುತ್ತವೆ.",
                    "ಎಡ ಹೃತ್ಕುಕ್ಷಿಯ ಗೋಡೆ ಅತಿ ದಪ್ಪ ಏಕೆಂದರೆ ಅದು ಇಡೀ ದೇಹಕ್ಕೆ ರಕ್ತ "
                    "ಪಂಪ್ ಮಾಡಬೇಕು; ಇದು ಶ್ವಾಸಕೋಶದ ಚಿಕ್ಕ ಪ್ರಯಾಣಕ್ಕಿಂತ ಉದ್ದ ಮತ್ತು ಹೆಚ್ಚು "
                    "ಪ್ರತಿರೋಧವಿರುವ ಮಾರ್ಗ. ಎರಡೂ ಭಾಗಗಳು ಒಟ್ಟಿಗೆ ಬಡಿಯುತ್ತವೆ: ಮೊದಲು "
                    "ಹೃತ್ಕರ್ಣಗಳು ಸಂಕೋಚಿಸಿ ಹೃತ್ಕುಕ್ಷಿಗಳನ್ನು ತುಂಬಿಸುತ್ತವೆ, ನಂತರ "
                    "ಹೃತ್ಕುಕ್ಷಿಗಳು ಸಂಕೋಚಿಸಿ ರಕ್ತವನ್ನು ಹೊರಗೆ ಕಳುಹಿಸುತ್ತವೆ.",
                ],
                "key_terms": [
                    {
                        "kn": "ಹೃತ್ಕರ್ಣ",
                        "en": "Atrium",
                        "meaning_kn": "ಹೃದಯದ ಮೇಲ್ಭಾಗದಲ್ಲಿರುವ, ರಕ್ತವನ್ನು ಸ್ವೀಕರಿಸುವ ಕೋಣೆ.",
                        "meaning_en": "An upper chamber of the heart that receives blood.",
                    },
                    {
                        "kn": "ಹೃತ್ಕುಕ್ಷಿ",
                        "en": "Ventricle",
                        "meaning_kn": "ಹೃದಯದ ಕೆಳಭಾಗದಲ್ಲಿರುವ, ರಕ್ತವನ್ನು ಹೊರಗೆ ಪಂಪ್ ಮಾಡುವ ಕೋಣೆ.",
                        "meaning_en": "A lower chamber of the heart that pumps blood out.",
                    },
                    {
                        "kn": "ಮಹಾಪಧಮನಿ",
                        "en": "Aorta",
                        "meaning_kn": "ಎಡ ಹೃತ್ಕುಕ್ಷಿಯಿಂದ ಹೊರಟು ದೇಹದ ಎಲ್ಲ ಭಾಗಗಳಿಗೆ ರಕ್ತ ಒಯ್ಯುವ ಅತಿ ದೊಡ್ಡ ಅಪಧಮನಿ.",
                        "meaning_en": "The largest artery, carrying blood from the left ventricle to the body.",
                    },
                    {
                        "kn": "ಕವಾಟ",
                        "en": "Valve",
                        "meaning_kn": "ರಕ್ತ ಹಿಂದಕ್ಕೆ ಹರಿಯದಂತೆ ತಡೆಯುವ ಬಾಗಿಲಿನಂತಹ ರಚನೆ.",
                        "meaning_en": "A flap-like structure that stops blood from flowing backwards.",
                    },
                ],
                "example_en": (
                    "Put two fingers on the side of your wrist. Each beat you feel is the left "
                    "ventricle pushing blood into the arteries, and the pause between beats is the "
                    "chambers refilling."
                ),
                "example_kn": (
                    "ನಿಮ್ಮ ಮಣಿಕಟ್ಟಿನ ಪಕ್ಕದಲ್ಲಿ ಎರಡು ಬೆರಳುಗಳನ್ನು ಇಡಿ. ನೀವು ಅನುಭವಿಸುವ ಪ್ರತಿ "
                    "ಬಡಿತವೂ ಎಡ ಹೃತ್ಕುಕ್ಷಿ ರಕ್ತವನ್ನು ಅಪಧಮನಿಗಳಿಗೆ ತಳ್ಳುವುದು; ಬಡಿತಗಳ "
                    "ನಡುವಿನ ವಿರಾಮದಲ್ಲಿ ಕೋಣೆಗಳು ಮತ್ತೆ ತುಂಬಿಕೊಳ್ಳುತ್ತವೆ."
                ),
            },
            {
                "title_en": "Blood circulation: two loops, one heart",
                "title_kn": "ರಕ್ತ ಪರಿಚಲನೆ: ಎರಡು ಚಕ್ರಗಳು, ಒಂದೇ ಹೃದಯ",
                "objectives_en": [
                    "Trace the pulmonary and systemic circulation paths.",
                    "Distinguish oxygen-rich from oxygen-poor blood.",
                    "Explain why a blockage in a coronary artery is dangerous.",
                ],
                "objectives_kn": [
                    "ಶ್ವಾಸಕೋಶೀಯ ಮತ್ತು ದೇಹ ಪರಿಚಲನೆಯ ಹಾದಿಗಳನ್ನು ಗುರುತಿಸುವುದು.",
                    "ಆಮ್ಲಜನಕಯುಕ್ತ ಮತ್ತು ಆಮ್ಲಜನಕ ಕಡಿಮೆ ಇರುವ ರಕ್ತವನ್ನು ಪ್ರತ್ಯೇಕಿಸುವುದು.",
                    "ಹೃದಯದ ಅಪಧಮನಿಯಲ್ಲಿ ಅಡಚಣೆ ಏಕೆ ಅಪಾಯಕಾರಿ ಎಂದು ವಿವರಿಸುವುದು.",
                ],
                "body_en": [
                    "Blood does not simply go round in one circle. It makes two loops that both "
                    "pass through the heart. In the shorter loop, the right ventricle sends "
                    "oxygen-poor blood to the lungs, where it picks up oxygen and gives out carbon "
                    "dioxide, and it returns to the left atrium. In the longer loop, the left "
                    "ventricle sends this oxygen-rich blood to the body, where tissues take the "
                    "oxygen, and the blood returns to the right atrium.",
                    "Because the two loops are separate, oxygen-rich and oxygen-poor blood do not "
                    "mix inside a healthy heart. That is why the left side of the heart is drawn "
                    "in red diagrams and the right side in blue. Blood moves fastest in arteries, "
                    "slows in capillaries where exchange happens, and returns at low pressure in "
                    "veins, helped by valves and by the squeezing of muscles around them.",
                    "The heart muscle needs blood too. Its own supply comes from the coronary "
                    "arteries, which branch from the aorta just above the heart. If one of these "
                    "narrows, part of the heart muscle is starved of oxygen, which causes chest "
                    "pain and can damage the muscle; this is why doctors treat blocked coronary "
                    "arteries urgently.",
                ],
                "body_kn": [
                    "ರಕ್ತವು ಒಂದೇ ವೃತ್ತದಲ್ಲಿ ಸುತ್ತುವುದಿಲ್ಲ. ಅದು ಎರಡು ಚಕ್ರಗಳನ್ನು "
                    "ಮಾಡುತ್ತದೆ; ಎರಡೂ ಹೃದಯದ ಮೂಲಕ ಹಾದುಹೋಗುತ್ತವೆ. ಚಿಕ್ಕ ಚಕ್ರದಲ್ಲಿ ಬಲ "
                    "ಹೃತ್ಕುಕ್ಷಿ ಆಮ್ಲಜನಕ ಕಡಿಮೆ ಇರುವ ರಕ್ತವನ್ನು ಶ್ವಾಸಕೋಶಕ್ಕೆ ಕಳುಹಿಸುತ್ತದೆ; "
                    "ಅಲ್ಲಿ ಆಮ್ಲಜನಕ ಸೇರಿಸಿಕೊಂಡು ಇಂಗಾಲದ ಡೈಆಕ್ಸೈಡ್ ಬಿಡುಗಡೆ ಮಾಡಿ ಎಡ "
                    "ಹೃತ್ಕರ್ಣಕ್ಕೆ ಹಿಂತಿರುಗುತ್ತದೆ. ಉದ್ದ ಚಕ್ರದಲ್ಲಿ ಎಡ ಹೃತ್ಕುಕ್ಷಿ ಈ "
                    "ಆಮ್ಲಜನಕಯುಕ್ತ ರಕ್ತವನ್ನು ದೇಹಕ್ಕೆ ಕಳುಹಿಸುತ್ತದೆ; ಅಲ್ಲಿ ಅಂಗಾಂಶಗಳು "
                    "ಆಮ್ಲಜನಕ ತೆಗೆದುಕೊಂಡು ರಕ್ತ ಬಲ ಹೃತ್ಕರ್ಣಕ್ಕೆ ಹಿಂತಿರುಗುತ್ತದೆ.",
                    "ಎರಡು ಚಕ್ರಗಳು ಪ್ರತ್ಯೇಕವಾಗಿರುವುದರಿಂದ ಆರೋಗ್ಯವಂತ ಹೃದಯದಲ್ಲಿ "
                    "ಆಮ್ಲಜನಕಯುಕ್ತ ಮತ್ತು ಆಮ್ಲಜನಕ ಕಡಿಮೆ ಇರುವ ರಕ್ತ ಬೆರೆಯುವುದಿಲ್ಲ; "
                    "ಆದ್ದರಿಂದಲೇ ಚಿತ್ರಗಳಲ್ಲಿ ಹೃದಯದ ಎಡ ಭಾಗವನ್ನು ಕೆಂಪು ಮತ್ತು ಬಲ ಭಾಗವನ್ನು "
                    "ನೀಲಿ ಬಣ್ಣದಲ್ಲಿ ತೋರಿಸುತ್ತಾರೆ. ರಕ್ತ ಅಪಧಮನಿಗಳಲ್ಲಿ ಅತಿ ವೇಗವಾಗಿ, "
                    "ವಿನಿಮಯ ನಡೆಯುವ ಕೆಶಿಕೆಗಳಲ್ಲಿ ನಿಧಾನವಾಗಿ, ಮತ್ತು ಅಭಿಧಮನಿಗಳಲ್ಲಿ ಕಡಿಮೆ "
                    "ಒತ್ತಡದಲ್ಲಿ ಹಿಂತಿರುಗುತ್ತದೆ; ಇದಕ್ಕೆ ಕವಾಟಗಳು ಮತ್ತು ಸುತ್ತಲಿನ "
                    "ಸ್ನಾಯುಗಳ ಸಂಕೋಚನ ಸಹಾಯ ಮಾಡುತ್ತವೆ.",
                    "ಹೃದಯದ ಸ್ನಾಯುವಿಗೂ ರಕ್ತ ಬೇಕು. ಅದರ ಪೂರೈಕೆ ಮಹಾಪಧಮನಿಯಿಂದ "
                    "ಕವಲೊಡೆಯುವ ಹೃದಯ ಅಪಧಮನಿಗಳಿಂದ ಬರುತ್ತದೆ. ಇವುಗಳಲ್ಲಿ ಒಂದು ಕಿರಿದಾದರೆ "
                    "ಹೃದಯದ ಸ್ನಾಯುವಿನ ಒಂದು ಭಾಗಕ್ಕೆ ಆಮ್ಲಜನಕ ಸಿಗದೆ ಎದೆನೋವು ಉಂಟಾಗಿ "
                    "ಸ್ನಾಯುವಿಗೆ ಹಾನಿಯಾಗಬಹುದು; ಆದ್ದರಿಂದ ಅಡಚಣೆಯಾದ ಹೃದಯ ಅಪಧಮನಿಗಳಿಗೆ "
                    "ತಕ್ಷಣ ಚಿಕಿತ್ಸೆ ನೀಡಲಾಗುತ್ತದೆ.",
                ],
                "key_terms": [
                    {
                        "kn": "ಕೆಶಿಕೆ",
                        "en": "Capillary",
                        "meaning_kn": "ಅತಿ ತೆಳುವಾದ ರಕ್ತನಾಳ; ಇಲ್ಲಿ ಆಮ್ಲಜನಕ ಮತ್ತು ಪೋಷಕಾಂಶ ಅಂಗಾಂಶಗಳಿಗೆ ಸೇರುತ್ತವೆ.",
                        "meaning_en": "The thinnest blood vessel, where oxygen and nutrients enter tissues.",
                    },
                    {
                        "kn": "ಅಪಧಮನಿ",
                        "en": "Artery",
                        "meaning_kn": "ಹೃದಯದಿಂದ ರಕ್ತವನ್ನು ಹೊರಗೆ ಒಯ್ಯುವ ದಪ್ಪ, ಸ್ಥಿತಿಸ್ಥಾಪಕ ರಕ್ತನಾಳ.",
                        "meaning_en": "A thick, elastic vessel that carries blood away from the heart.",
                    },
                    {
                        "kn": "ಅಭಿಧಮನಿ",
                        "en": "Vein",
                        "meaning_kn": "ರಕ್ತವನ್ನು ಹೃದಯಕ್ಕೆ ಹಿಂತಿರುಗಿಸುವ ರಕ್ತನಾಳ; ಇದರಲ್ಲಿ ಕವಾಟಗಳಿರುತ್ತವೆ.",
                        "meaning_en": "A vessel that returns blood to the heart, usually with valves inside.",
                    },
                ],
                "example_en": (
                    "During a race your leg muscles need more oxygen, so your heart beats faster and "
                    "your breathing deepens. Both loops speed up together to carry oxygen in and "
                    "carbon dioxide out."
                ),
                "example_kn": (
                    "ಓಟದ ಸಮಯದಲ್ಲಿ ಕಾಲಿನ ಸ್ನಾಯುಗಳಿಗೆ ಹೆಚ್ಚು ಆಮ್ಲಜನಕ ಬೇಕು; ಆದ್ದರಿಂದ "
                    "ಹೃದಯಬಡಿತ ಹೆಚ್ಚಾಗಿ ಉಸಿರಾಟ ಆಳವಾಗುತ್ತದೆ. ಆಮ್ಲಜನಕ ಒಳಗೆ ಮತ್ತು "
                    "ಇಂಗಾಲದ ಡೈಆಕ್ಸೈಡ್ ಹೊರಗೆ ಸಾಗಿಸಲು ಎರಡೂ ಚಕ್ರಗಳು ಒಟ್ಟಿಗೆ ವೇಗಗೊಳ್ಳುತ್ತವೆ."
                ),
            },
            {
                "title_en": "The nervous system: signals and reflexes",
                "title_kn": "ನರಮಂಡಲ: ಸಂಕೇತಗಳು ಮತ್ತು ಪ್ರತಿವರ್ತನಗಳು",
                "objectives_en": [
                    "Distinguish the central nervous system from the peripheral nervous system.",
                    "Describe how a message travels from a sense organ to a muscle.",
                    "Explain reflex action with an everyday example.",
                ],
                "objectives_kn": [
                    "ಕೇಂದ್ರ ನರಮಂಡಲ ಮತ್ತು ಪರಿಧಿಯ ನರಮಂಡಲವನ್ನು ಪ್ರತ್ಯೇಕಿಸುವುದು.",
                    "ಇಂದ್ರಿಯಾಂಗದಿಂದ ಸ್ನಾಯುವಿಗೆ ಸಂದೇಶ ಹೇಗೆ ಸಾಗುತ್ತದೆ ಎಂದು ವಿವರಿಸುವುದು.",
                    "ದಿನನಿತ್ಯದ ಉದಾಹರಣೆಯೊಂದಿಗೆ ಪ್ರತಿವರ್ತನ ಕ್ರಿಯೆ ವಿವರಿಸುವುದು.",
                ],
                "body_en": [
                    "The nervous system is the body's signalling network. It has two parts: the "
                    "central nervous system, made of the brain and spinal cord, and the peripheral "
                    "nervous system, which is all the nerves branching out to the rest of the body. "
                    "The brain decides and the spinal cord carries, while the peripheral nerves "
                    "collect information and deliver instructions.",
                    "A neuron is a nerve cell with a long fibre that carries an electrical impulse. "
                    "Signals travel from a sense organ, such as skin or the eye, along a sensory "
                    "nerve to the spinal cord and brain; the brain interprets the signal and sends "
                    "an impulse along a motor nerve to a muscle or gland, which responds.",
                    "Some responses do not wait for the brain. In a reflex action the spinal cord "
                    "itself links the incoming signal to an outgoing one, so the muscle acts "
                    "immediately. That is why your hand leaves a hot vessel before you consciously "
                    "feel the pain. Reflexes protect the body while the brain is still processing "
                    "what happened.",
                ],
                "body_kn": [
                    "ನರಮಂಡಲವು ದೇಹದ ಸಂಕೇತ ಜಾಲ. ಇದಕ್ಕೆ ಎರಡು ಭಾಗಗಳಿವೆ: ಮಿದುಳು ಮತ್ತು "
                    "ಬೆನ್ನುಹುರಿಯಿಂದಾದ ಕೇಂದ್ರ ನರಮಂಡಲ, ಮತ್ತು ದೇಹದ ಉಳಿದ ಭಾಗಗಳಿಗೆ "
                    "ಹರಡುವ ನರಗಳಿಂದಾದ ಪರಿಧಿಯ ನರಮಂಡಲ. ಮಿದುಳು ನಿರ್ಧರಿಸುತ್ತದೆ, "
                    "ಬೆನ್ನುಹುರಿ ಸಾಗಿಸುತ್ತದೆ; ಪರಿಧಿಯ ನರಗಳು ಮಾಹಿತಿ ಸಂಗ್ರಹಿಸಿ ಸೂಚನೆ "
                    "ತಲುಪಿಸುತ್ತವೆ.",
                    "ನ್ಯೂರಾನ್ ಎಂದರೆ ಉದ್ದವಾದ ನಾರಿನಿಂದ ವಿದ್ಯುತ್ ಸ್ಪಂದನವನ್ನು "
                    "ಸಾಗಿಸುವ ನರಕಣ. ಚರ್ಮ ಅಥವಾ ಕಣ್ಣಿನಂತಹ ಇಂದ್ರಿಯಾಂಗದಿಂದ ಸಂಕೇತ "
                    "ಸಂವೇದಿ ನರದ ಮೂಲಕ ಬೆನ್ನುಹುರಿ ಮತ್ತು ಮಿದುಳಿಗೆ ಹೋಗುತ್ತದೆ; ಮಿದುಳು "
                    "ಅದನ್ನು ಅರ್ಥೈಸಿ ಚಾಲಕ ನರದ ಮೂಲಕ ಸ್ನಾಯು ಅಥವಾ ಗ್ರಂಥಿಗೆ ಸ್ಪಂದನ "
                    "ಕಳುಹಿಸುತ್ತದೆ; ಅದು ಪ್ರತಿಕ್ರಿಯಿಸುತ್ತದೆ.",
                    "ಕೆಲವು ಪ್ರತಿಕ್ರಿಯೆಗಳು ಮಿದುಳಿಗೆ ಕಾಯುವುದಿಲ್ಲ. ಪ್ರತಿವರ್ತನ "
                    "ಕ್ರಿಯೆಯಲ್ಲಿ ಬೆನ್ನುಹುರಿಯೇ ಬರುವ ಸಂಕೇತವನ್ನು ಹೊರಹೋಗುವ ಸಂಕೇತಕ್ಕೆ "
                    "ಜೋಡಿಸುತ್ತದೆ; ಹಾಗಾಗಿ ಸ್ನಾಯು ತಕ್ಷಣ ಕ್ರಿಯೆ ನಡೆಸುತ್ತದೆ. ಬಿಸಿ ಪಾತ್ರೆಗೆ "
                    "ಕೈ ತಗುಲಿದಾಗ ನೋವು ಅರಿವಿಗೆ ಬರುವ ಮೊದಲೇ ಕೈ ಹಿಂದೆ ಸರಿಯುವುದು "
                    "ಇದಕ್ಕೆ ಕಾರಣ. ಮಿದುಳು ಏನಾಯಿತು ಎಂದು ಯೋಚಿಸುತ್ತಿರುವಾಗಲೇ "
                    "ಪ್ರತಿವರ್ತನಗಳು ದೇಹವನ್ನು ರಕ್ಷಿಸುತ್ತವೆ.",
                ],
                "key_terms": [
                    {
                        "kn": "ನ್ಯೂರಾನ್",
                        "en": "Neuron",
                        "meaning_kn": "ವಿದ್ಯುತ್ ಸ್ಪಂದನವನ್ನು ಸಾಗಿಸುವ ನರಕಣ.",
                        "meaning_en": "A nerve cell that carries electrical impulses.",
                    },
                    {
                        "kn": "ಪ್ರತಿವರ್ತನ",
                        "en": "Reflex action",
                        "meaning_kn": "ಮಿದುಳಿನ ಉದ್ದೇಶಪೂರ್ವಕ ಯೋಚನೆ ಇಲ್ಲದೆ ತಕ್ಷಣ ನಡೆಯುವ ರಕ್ಷಣಾತ್ಮಕ ಪ್ರತಿಕ್ರಿಯೆ.",
                        "meaning_en": "A fast, automatic protective response that does not wait for conscious thought.",
                    },
                    {
                        "kn": "ಬೆನ್ನುಹುರಿ",
                        "en": "Spinal cord",
                        "meaning_kn": "ಮಿದುಳಿನಿಂದ ದೇಹದ ಕೆಳಭಾಗಕ್ಕೆ ಹೋಗುವ ಮುಖ್ಯ ನರಮಾರ್ಗ.",
                        "meaning_en": "The main nerve pathway running from the brain down the back.",
                    },
                ],
                "example_en": (
                    "If a speck of dust touches your eye, you blink before you decide to. The "
                    "signal is short-circuited through the brainstem, which is why the blink feels "
                    "instant."
                ),
                "example_kn": (
                    "ಕಣ್ಣಿಗೆ ಧೂಳಿನ ಕಣ ಬಿದ್ದರೆ ನೀವು ನಿರ್ಧರಿಸುವ ಮೊದಲೇ ಕಣ್ಣು ಮಿಟುಕಿಸುತ್ತದೆ. "
                    "ಸಂಕೇತವು ಮಿದುಳು ಕಾಂಡದ ಮೂಲಕ ಸಂಕ್ಷಿಪ್ತಗೊಳ್ಳುತ್ತದೆ; ಆದ್ದರಿಂದಲೇ ಆ "
                    "ಮಿಟುಕಿಸುವಿಕೆ ತಕ್ಷಣದ್ದು ಎನಿಸುತ್ತದೆ."
                ),
            },
            {
                "title_en": "Blood and blood vessels",
                "title_kn": "ರಕ್ತ ಮತ್ತು ರಕ್ತನಾಳಗಳು",
                "objectives_en": [
                    "Name the main components of blood and one job of each.",
                    "Compare arteries, veins and capillaries.",
                    "Explain why a small cut stops bleeding on its own.",
                ],
                "objectives_kn": [
                    "ರಕ್ತದ ಮುಖ್ಯ ಘಟಕಗಳನ್ನು ಹೆಸರಿಸಿ ಪ್ರತಿಯೊಂದರ ಒಂದು ಕೆಲಸ ತಿಳಿಸುವುದು.",
                    "ಅಪಧಮನಿ, ಅಭಿಧಮನಿ ಮತ್ತು ಕೆಶಿಕೆಗಳನ್ನು ಹೋಲಿಸುವುದು.",
                    "ಸಣ್ಣ ಗಾಯದಿಂದ ರಕ್ತಸ್ರಾವ ತಾನಾಗಿಯೇ ನಿಲ್ಲುವುದೇಕೆ ಎಂದು ವಿವರಿಸುವುದು.",
                ],
                "body_en": [
                    "Blood is a liquid tissue that carries everything the body needs. Plasma is the "
                    "pale liquid part that dissolves food, salts and waste. Red blood cells contain "
                    "haemoglobin, which picks up oxygen in the lungs and releases it in tissues. "
                    "White blood cells defend the body against germs, and platelets are fragments "
                    "that clump together to plug a torn vessel.",
                    "The vessels form a network of three kinds. Arteries carry blood away from the "
                    "heart under high pressure and have thick elastic walls. Veins carry blood back "
                    "at low pressure and have valves so blood cannot slide backwards. Capillaries "
                    "are microscopic vessels with walls only one cell thick, so oxygen, glucose and "
                    "waste can pass between blood and tissue.",
                    "When you get a small cut, platelets stick to the damaged edges and release "
                    "substances that start a chain of reactions; threads of a protein called fibrin "
                    "form a net that traps red cells and seals the wound. This is why a small cut "
                    "stops bleeding in a few minutes without any help.",
                ],
                "body_kn": [
                    "ರಕ್ತವು ದೇಹಕ್ಕೆ ಬೇಕಾದ ಎಲ್ಲವನ್ನೂ ಸಾಗಿಸುವ ದ್ರವ ಅಂಗಾಂಶ. ಪ್ಲಾಸ್ಮಾ ಎಂಬ "
                    "ತಿಳಿ ದ್ರವ ಭಾಗ ಆಹಾರ, ಲವಣ ಮತ್ತು ತ್ಯಾಜ್ಯವನ್ನು ಕರಗಿಸುತ್ತದೆ. ಕೆಂಪು ರಕ್ತ "
                    "ಕಣಗಳಲ್ಲಿರುವ ಹಿಮೋಗ್ಲೋಬಿನ್ ಶ್ವಾಸಕೋಶದಲ್ಲಿ ಆಮ್ಲಜನಕ ಸೇರಿಸಿಕೊಂಡು "
                    "ಅಂಗಾಂಶಗಳಲ್ಲಿ ಬಿಡುಗಡೆ ಮಾಡುತ್ತದೆ. ಬಿಳಿ ರಕ್ತ ಕಣಗಳು ರೋಗಾಣುಗಳಿಂದ "
                    "ರಕ್ಷಿಸುತ್ತವೆ; ಪ್ಲೇಟ್ಲೆಟ್ ಎಂಬ ಕಣಭಾಗಗಳು ಸೇರಿ ಹರಿದ ರಕ್ತನಾಳವನ್ನು "
                    "ಮುಚ್ಚುತ್ತವೆ.",
                    "ರಕ್ತನಾಳಗಳು ಮೂರು ಬಗೆಯ ಜಾಲವನ್ನು ರೂಪಿಸುತ್ತವೆ. ಅಪಧಮನಿಗಳು ಹೃದಯದಿಂದ "
                    "ಹೊರಕ್ಕೆ ಹೆಚ್ಚು ಒತ್ತಡದಲ್ಲಿ ರಕ್ತ ಒಯ್ಯುತ್ತವೆ; ಅವುಗಳ ಗೋಡೆ ದಪ್ಪ ಮತ್ತು "
                    "ಸ್ಥಿತಿಸ್ಥಾಪಕ. ಅಭಿಧಮನಿಗಳು ಕಡಿಮೆ ಒತ್ತಡದಲ್ಲಿ ರಕ್ತವನ್ನು ಹಿಂದಕ್ಕೆ "
                    "ತರುತ್ತವೆ; ರಕ್ತ ಜಾರಿ ಹಿಂದಕ್ಕೆ ಹೋಗದಂತೆ ಅವುಗಳಲ್ಲಿ ಕವಾಟಗಳಿವೆ. "
                    "ಕೆಶಿಕೆಗಳು ಸೂಕ್ಷ್ಮ ರಕ್ತನಾಳಗಳು; ಅವುಗಳ ಗೋಡೆ ಒಂದೇ ಕಣದಷ್ಟು "
                    "ತೆಳುವಾಗಿರುವುದರಿಂದ ಆಮ್ಲಜನಕ, ಗ್ಲೂಕೋಸ್ ಮತ್ತು ತ್ಯಾಜ್ಯ ರಕ್ತ ಮತ್ತು "
                    "ಅಂಗಾಂಶದ ನಡುವೆ ವಿನಿಮಯವಾಗುತ್ತವೆ.",
                    "ಸಣ್ಣ ಗಾಯವಾದಾಗ ಪ್ಲೇಟ್ಲೆಟ್‌ಗಳು ಹರಿದ ಅಂಚುಗಳಿಗೆ ಅಂಟಿಕೊಂಡು "
                    "ರಾಸಾಯನಿಕ ಕ್ರಿಯೆಗಳ ಸರಣಿ ಆರಂಭಿಸುತ್ತವೆ; ಫೈಬ್ರಿನ್ ಎಂಬ ಪ್ರೋಟೀನ್ "
                    "ನೂಲುಗಳು ಬಲೆಯಂತೆ ರೂಪುಗೊಂಡು ಕೆಂಪು ಕಣಗಳನ್ನು ಹಿಡಿದು ಗಾಯವನ್ನು "
                    "ಮುಚ್ಚುತ್ತವೆ. ಆದ್ದರಿಂದಲೇ ಸಣ್ಣ ಗಾಯದಿಂದ ರಕ್ತಸ್ರಾವ ಸಹಾಯವಿಲ್ಲದೆಯೂ "
                    "ಕೆಲವು ನಿಮಿಷಗಳಲ್ಲಿ ನಿಲ್ಲುತ್ತದೆ.",
                ],
                "key_terms": [
                    {
                        "kn": "ಹಿಮೋಗ್ಲೋಬಿನ್",
                        "en": "Haemoglobin",
                        "meaning_kn": "ಕೆಂಪು ರಕ್ತ ಕಣಗಳಲ್ಲಿರುವ, ಆಮ್ಲಜನಕವನ್ನು ಹಿಡಿದಿಟ್ಟುಕೊಳ್ಳುವ ವರ್ಣದ್ರವ್ಯ.",
                        "meaning_en": "The red pigment in red blood cells that carries oxygen.",
                    },
                    {
                        "kn": "ಪ್ಲೇಟ್ಲೆಟ್",
                        "en": "Platelet",
                        "meaning_kn": "ರಕ್ತಸ್ರಾವ ನಿಲ್ಲಿಸಲು ಸಹಾಯ ಮಾಡುವ ಸಣ್ಣ ಕಣಭಾಗ.",
                        "meaning_en": "A small cell fragment that helps stop bleeding.",
                    },
                    {
                        "kn": "ಪ್ಲಾಸ್ಮಾ",
                        "en": "Plasma",
                        "meaning_kn": "ರಕ್ತದ ತಿಳಿ ದ್ರವ ಭಾಗ; ಆಹಾರ, ಲವಣ ಮತ್ತು ತ್ಯಾಜ್ಯವನ್ನು ಕರಗಿಸುತ್ತದೆ.",
                        "meaning_en": "The pale liquid part of blood that dissolves food, salts and waste.",
                    },
                ],
                "example_en": (
                    "A donor's blood is checked before transfusion because the marker molecules on "
                    "red cells must match the patient's; a mismatch makes the immune system attack "
                    "the donated cells."
                ),
                "example_kn": (
                    "ರಕ್ತ ನೀಡುವ ಮೊದಲು ದಾನಿಯ ರಕ್ತವನ್ನು ಪರೀಕ್ಷಿಸಲಾಗುತ್ತದೆ ಏಕೆಂದರೆ ಕೆಂಪು "
                    "ಕಣಗಳ ಮೇಲ್ಮೈ ಗುರುತುಗಳು ರೋಗಿಯ ರಕ್ತಕ್ಕೆ ಹೊಂದಬೇಕು; ಹೊಂದದಿದ್ದರೆ "
                    "ರೋಗನಿರೋಧಕ ವ್ಯವಸ್ಥೆ ದಾನಿಯ ಕಣಗಳ ಮೇಲೆ ದಾಳಿ ಮಾಡುತ್ತದೆ."
                ),
            },
        ],
        "notes_kn": [
            "ಮಿದುಳಿನ ಮುಖ್ಯ ಭಾಗಗಳು: ಸೆರೆಬ್ರಮ್ (ಯೋಚನೆ, ನೆನಪು), ಸೆರೆಬೆಲ್ಲಮ್ (ಸಮತೋಲನ, ಚಲನೆ), ಮಿದುಳು ಕಾಂಡ (ಉಸಿರಾಟ, ಹೃದಯಬಡಿತ).",
            "ಮಿದುಳಿನ ರಕ್ಷಣೆ: ತಲೆಬುರುಡೆ, ಮೆನಿಂಜಸ್ ಪೊರೆಗಳು, ಮಿದುಳು ಬೆನ್ನುಹುರಿ ದ್ರವ.",
            "ಹೃದಯದ ನಾಲ್ಕು ಕೋಣೆಗಳು: ಬಲ ಹೃತ್ಕರ್ಣ, ಬಲ ಹೃತ್ಕುಕ್ಷಿ, ಎಡ ಹೃತ್ಕರ್ಣ, ಎಡ ಹೃತ್ಕುಕ್ಷಿ.",
            "ಎಡ ಹೃತ್ಕುಕ್ಷಿಯ ಗೋಡೆ ದಪ್ಪ; ಅದು ಇಡೀ ದೇಹಕ್ಕೆ ರಕ್ತ ಪಂಪ್ ಮಾಡುತ್ತದೆ.",
            "ರಕ್ತದ ಹಾದಿ: ದೇಹ → ಮಹಾ ಅಭಿಧಮನಿ → ಬಲ ಹೃತ್ಕರ್ಣ → ಬಲ ಹೃತ್ಕುಕ್ಷಿ → ಶ್ವಾಸಕೋಶ → ಎಡ ಹೃತ್ಕರ್ಣ → ಎಡ ಹೃತ್ಕುಕ್ಷಿ → ಮಹಾಪಧಮನಿ → ದೇಹ.",
            "ಅಪಧಮನಿ: ಹೃದಯದಿಂದ ಹೊರಕ್ಕೆ; ಅಭಿಧಮನಿ: ಹೃದಯಕ್ಕೆ ಒಳಕ್ಕೆ; ಕೆಶಿಕೆ: ಅತಿ ತೆಳು, ವಿನಿಮಯದ ಸ್ಥಳ.",
            "ರಕ್ತದ ಘಟಕಗಳು: ಪ್ಲಾಸ್ಮಾ, ಕೆಂಪು ರಕ್ತ ಕಣ, ಬಿಳಿ ರಕ್ತ ಕಣ, ಪ್ಲೇಟ್ಲೆಟ್.",
            "ಪ್ರತಿವರ್ತನ ಕ್ರಿಯೆ ಬೆನ್ನುಹುರಿಯಲ್ಲಿ ಪೂರ್ಣಗೊಳ್ಳುತ್ತದೆ; ಆದ್ದರಿಂದ ಅತಿ ವೇಗ.",
        ],
        "notes_en": [
            "Brain parts: cerebrum (thinking, memory, senses), cerebellum (balance, smooth movement), brainstem (breathing, heartbeat).",
            "The brain is protected by the skull, three meninges and cerebrospinal fluid.",
            "Heart chambers: right atrium, right ventricle, left atrium, left ventricle.",
            "The left ventricle wall is thickest because it pumps blood around the whole body.",
            "Blood path: body → vena cava → right atrium → right ventricle → lungs → left atrium → left ventricle → aorta → body.",
            "Arteries carry blood away from the heart; veins return it; capillaries are one cell thick for exchange.",
            "Blood components: plasma, red blood cells, white blood cells, platelets.",
            "A reflex action is completed in the spinal cord, which is why it is faster than a deliberate action.",
        ],
        "videos": [
            {
                "title": "ಮಾನವ ಹೃದಯ — ಕನ್ನಡ ವಿವರಣೆ",
                "language": "kn",
                "topic": "Human heart",
                "search_query": "ಮಾನವ ಹೃದಯ ಕನ್ನಡ 8ನೇ ತರಗತಿ ವಿಜ್ಞಾನ ಕೋಣೆಗಳು ರಕ್ತ ಪರಿಚಲನೆ",
            },
            {
                "title": "Human heart structure for Class 8",
                "language": "en",
                "topic": "Human heart",
                "search_query": "human heart four chambers class 8 circulatory system explanation",
            },
            {
                "title": "ನರಮಂಡಲ ಮತ್ತು ಮಿದುಳು — ಕನ್ನಡ",
                "language": "kn",
                "topic": "Nervous system",
                "search_query": "ನರಮಂಡಲ ಮಿದುಳು ಕನ್ನಡ 8ನೇ ತರಗತಿ ವಿಜ್ಞಾನ ಪ್ರತಿವರ್ತನ ಕ್ರಿಯೆ",
            },
            {
                "title": "Nervous system and reflexes for Class 8",
                "language": "en",
                "topic": "Nervous system",
                "search_query": "nervous system neurons reflex action class 8 science lesson",
            },
        ],
        "quiz": [
            {
                "question_en": "Which part of the brain keeps balance and makes movement smooth?",
                "question_kn": "ಸಮತೋಲನ ಕಾಪಾಡಿ ಚಲನೆಯನ್ನು ನಯವಾಗಿಸುವ ಮಿದುಳಿನ ಭಾಗ ಯಾವುದು?",
                "options_en": ["Cerebrum", "Cerebellum", "Brainstem", "Spinal cord"],
                "options_kn": ["ಸೆರೆಬ್ರಮ್", "ಸೆರೆಬೆಲ್ಲಮ್", "ಮಿದುಳು ಕಾಂಡ", "ಬೆನ್ನುಹುರಿ"],
                "correct_index": 1,
                "explanation_en": "The cerebellum coordinates balance and smooth, practised movement.",
                "explanation_kn": "ಸೆರೆಬೆಲ್ಲಮ್ ಸಮತೋಲನ ಮತ್ತು ಅಭ್ಯಾಸವಾದ ನಯವಾದ ಚಲನೆಯನ್ನು ಸಮನ್ವಯ ಮಾಡುತ್ತದೆ.",
                "difficulty": 1,
                "question_type": "mcq",
            },
            {
                "question_en": "How many chambers does the human heart have?",
                "question_kn": "ಮಾನವ ಹೃದಯಕ್ಕೆ ಎಷ್ಟು ಕೋಣೆಗಳಿವೆ?",
                "options_en": ["Two", "Three", "Four", "Five"],
                "options_kn": ["ಎರಡು", "ಮೂರು", "ನಾಲ್ಕು", "ಐದು"],
                "correct_index": 2,
                "explanation_en": "Two atria receive blood and two ventricles pump it out.",
                "explanation_kn": "ಎರಡು ಹೃತ್ಕರ್ಣಗಳು ರಕ್ತ ಸ್ವೀಕರಿಸುತ್ತವೆ, ಎರಡು ಹೃತ್ಕುಕ್ಷಿಗಳು ಅದನ್ನು ಪಂಪ್ ಮಾಡುತ್ತವೆ.",
                "difficulty": 1,
                "question_type": "mcq",
            },
            {
                "question_en": "Blood from the lungs returns to which chamber of the heart?",
                "question_kn": "ಶ್ವಾಸಕೋಶದಿಂದ ಬರುವ ರಕ್ತ ಹೃದಯದ ಯಾವ ಕೋಣೆಗೆ ಸೇರುತ್ತದೆ?",
                "options_en": ["Right atrium", "Left atrium", "Right ventricle", "Left ventricle"],
                "options_kn": ["ಬಲ ಹೃತ್ಕರ್ಣ", "ಎಡ ಹೃತ್ಕರ್ಣ", "ಬಲ ಹೃತ್ಕುಕ್ಷಿ", "ಎಡ ಹೃತ್ಕುಕ್ಷಿ"],
                "correct_index": 1,
                "explanation_en": "Pulmonary veins bring oxygen-rich blood into the left atrium.",
                "explanation_kn": "ಶ್ವಾಸಕೋಶೀಯ ಅಭಿಧಮನಿಗಳು ಆಮ್ಲಜನಕಯುಕ್ತ ರಕ್ತವನ್ನು ಎಡ ಹೃತ್ಕರ್ಣಕ್ಕೆ ತರುತ್ತವೆ.",
                "difficulty": 2,
                "question_type": "mcq",
            },
            {
                "question_en": "Which vessel carries blood away from the heart at high pressure?",
                "question_kn": "ಹೆಚ್ಚು ಒತ್ತಡದಲ್ಲಿ ಹೃದಯದಿಂದ ರಕ್ತವನ್ನು ಹೊರಗೆ ಒಯ್ಯುವ ರಕ್ತನಾಳ ಯಾವುದು?",
                "options_en": ["Vein", "Artery", "Capillary", "Nerve"],
                "options_kn": ["ಅಭಿಧಮನಿ", "ಅಪಧಮನಿ", "ಕೆಶಿಕೆ", "ನರ"],
                "correct_index": 1,
                "explanation_en": "Arteries have thick elastic walls for the pressure of each heartbeat.",
                "explanation_kn": "ಪ್ರತಿ ಹೃದಯಬಡಿತದ ಒತ್ತಡವನ್ನು ತಡೆಯಲು ಅಪಧಮನಿಗಳ ಗೋಡೆ ದಪ್ಪ ಮತ್ತು ಸ್ಥಿತಿಸ್ಥಾಪಕ.",
                "difficulty": 1,
                "question_type": "mcq",
            },
            {
                "question_en": "A reflex action is completed mainly in the…",
                "question_kn": "ಪ್ರತಿವರ್ತನ ಕ್ರಿಯೆ ಮುಖ್ಯವಾಗಿ ಎಲ್ಲಿ ಪೂರ್ಣಗೊಳ್ಳುತ್ತದೆ?",
                "options_en": ["Cerebrum", "Cerebellum", "Spinal cord", "Heart"],
                "options_kn": ["ಸೆರೆಬ್ರಮ್", "ಸೆರೆಬೆಲ್ಲಮ್", "ಬೆನ್ನುಹುರಿ", "ಹೃದಯ"],
                "correct_index": 2,
                "explanation_en": "The spinal cord links the incoming and outgoing signals directly, so the response is very fast.",
                "explanation_kn": "ಬೆನ್ನುಹುರಿ ಬರುವ ಮತ್ತು ಹೋಗುವ ಸಂಕೇತಗಳನ್ನು ನೇರವಾಗಿ ಜೋಡಿಸುವುದರಿಂದ ಪ್ರತಿಕ್ರಿಯೆ ಅತಿ ವೇಗವಾಗಿರುತ್ತದೆ.",
                "difficulty": 2,
                "question_type": "mcq",
            },
            {
                "question_en": "Haemoglobin in red blood cells carries oxygen.",
                "question_kn": "ಕೆಂಪು ರಕ್ತ ಕಣಗಳಲ್ಲಿರುವ ಹಿಮೋಗ್ಲೋಬಿನ್ ಆಮ್ಲಜನಕವನ್ನು ಸಾಗಿಸುತ್ತದೆ.",
                "options_en": ["True", "False"],
                "options_kn": ["ಸರಿ", "ತಪ್ಪು"],
                "correct_index": 0,
                "explanation_en": "Haemoglobin binds oxygen in the lungs and releases it in tissues.",
                "explanation_kn": "ಹಿಮೋಗ್ಲೋಬಿನ್ ಶ್ವಾಸಕೋಶದಲ್ಲಿ ಆಮ್ಲಜನಕವನ್ನು ಬಂಧಿಸಿ ಅಂಗಾಂಶಗಳಲ್ಲಿ ಬಿಡುಗಡೆ ಮಾಡುತ್ತದೆ.",
                "difficulty": 1,
                "question_type": "true_false",
            },
        ],
    },
)
