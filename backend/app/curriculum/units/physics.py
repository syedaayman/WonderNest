"""Physics units 3-5: electricity, forces, and light.

All text below is original WonderNest study material written for Class 8 students.
"""

UNITS: tuple[dict, ...] = (
    {
        "number": 3,
        "category": "physics",
        "is_enrichment": False,
        "title_en": "Electricity: Magnetic and Heating Effects",
        "title_kn": "ವಿದ್ಯುತ್: ಕಾಂತೀಯ ಮತ್ತು ಉಷ್ಣ ಪರಿಣಾಮಗಳು",
        "summary_en": (
            "Build a mental model of current flowing in a closed circuit, then see how that "
            "current heats wires and creates magnetism in motors, bells and cranes."
        ),
        "summary_kn": (
            "ಮುಚ್ಚಿದ ಮಂಡಲದಲ್ಲಿ ವಿದ್ಯುತ್ ಪ್ರವಾಹ ಹರಿಯುವ ಬಗ್ಗೆ ಕಲ್ಪನೆ ಮಾಡಿಕೊಳ್ಳಿ, "
            "ನಂತರ ಆ ಪ್ರವಾಹ ತಂತಿಗಳನ್ನು ಬಿಸಿ ಮಾಡುವುದು ಮತ್ತು ಮೋಟಾರ್, ಗಂಟೆ ಹಾಗೂ "
            "ಕ್ರೇನ್‌ಗಳಲ್ಲಿ ಕಾಂತತ್ವ ಉಂಟುಮಾಡುವುದನ್ನು ತಿಳಿಯಿರಿ."
        ),
        "estimated_minutes": 45,
        "visualizations": ["electricity"],
        "topics": [
            {
                "title_en": "A simple electric circuit",
                "title_kn": "ಸರಳ ವಿದ್ಯುತ್ ಮಂಡಲ",
                "objectives_en": [
                    "Draw a circuit with a cell, switch, wire and bulb.",
                    "Explain why the bulb glows only when the switch is closed.",
                ],
                "objectives_kn": [
                    "ಒಂದು ಕೋಶ, ಸ್ವಿಚ್, ತಂತಿ ಮತ್ತು ಬಲ್ಬ್ ಇರುವ ಮಂಡಲವನ್ನು ಬರೆಯುವುದು.",
                    "ಸ್ವಿಚ್ ಮುಚ್ಚಿದಾಗ ಮಾತ್ರ ಬಲ್ಬ್ ಬೆಳಗುವುದು ಏಕೆ ಎಂಬುದನ್ನು ವಿವರಿಸುವುದು.",
                ],
                "body_en": [
                    "An electric circuit is a complete path that electric charges can travel along. "
                    "A cell pushes charges from its negative terminal, through the wire, the bulb "
                    "and the switch, back to its positive terminal. As long as that path is "
                    "unbroken, we say the circuit is closed and a current flows.",
                    "Open the switch and the path breaks: charges stop moving at once and the bulb "
                    "goes dark. This is why a torch that will not light usually has a loose "
                    "connection or a flat cell rather than a 'tired' bulb. Metals such as copper "
                    "let charges move easily and are used as wires; plastic and rubber resist them "
                    "and are used as insulation. Never experiment with the mains supply: cells are "
                    "safe for classroom circuits.",
                ],
                "body_kn": [
                    "ವಿದ್ಯುತ್ ಮಂಡಲ ಎಂದರೆ ವಿದ್ಯುತ್ ಆವೇಶಗಳು ಸಾಗಬಹುದಾದ ಪೂರ್ಣ ಮಾರ್ಗ. "
                    "ಕೋಶವು ಋಣ ತುದಿಯಿಂದ ಆವೇಶಗಳನ್ನು ತಂತಿ, ಬಲ್ಬ್ ಮತ್ತು ಸ್ವಿಚ್ "
                    "ಮೂಲಕ ತಳ್ಳಿ ಧನ ತುದಿಗೆ ಮರಳಿಸುತ್ತದೆ. ಆ ಮಾರ್ಗ ಎಲ್ಲಿಯೂ "
                    "ಕಡಿತಗೊಳ್ಳದಿದ್ದರೆ ಮಂಡಲ ಮುಚ್ಚಿದೆ ಎನ್ನುತ್ತೇವೆ ಮತ್ತು ಪ್ರವಾಹ "
                    "ಹರಿಯುತ್ತದೆ.",
                    "ಸ್ವಿಚ್ ತೆರೆದರೆ ಮಾರ್ಗ ಒಡೆಯುತ್ತದೆ: ಆವೇಶಗಳ ಚಲನೆ ತಕ್ಷಣ ನಿಲ್ಲುತ್ತದೆ "
                    "ಮತ್ತು ಬಲ್ಬ್ ಆರಿಹೋಗುತ್ತದೆ. ಬೆಳಗದ ಟಾರ್ಚ್‌ನಲ್ಲಿ ಸಾಮಾನ್ಯವಾಗಿ "
                    "ಸಡಿಲ ಸಂಪರ್ಕ ಅಥವಾ ಖಾಲಿಯಾದ ಕೋಶ ಇರುತ್ತದೆ, ಬಲ್ಬ್ "
                    "'ದಣಿದಿರುವುದಿಲ್ಲ'. ತಾಮ್ರದಂತಹ ಲೋಹಗಳು ಆವೇಶಗಳನ್ನು ಸುಲಭವಾಗಿ "
                    "ಸಾಗಿಸುತ್ತವೆ ಮತ್ತು ತಂತಿಗಳಾಗಿ ಬಳಕೆಯಾಗುತ್ತವೆ; ಪ್ಲಾಸ್ಟಿಕ್ ಮತ್ತು "
                    "ರಬ್ಬರ್ ಅವನ್ನು ತಡೆಯುತ್ತವೆ, ಆದ್ದರಿಂದ ಅವು ನಿರೋಧಕಗಳು. ಮನೆಯ "
                    "ಮುಖ್ಯ ವಿದ್ಯುತ್ ಸರಬರಾಜಿನೊಂದಿಗೆ ಎಂದೂ ಪ್ರಯೋಗ ಮಾಡಬೇಡಿ: "
                    "ತರಗತಿ ಮಂಡಲಗಳಿಗೆ ಕೋಶಗಳು ಸುರಕ್ಷಿತ.",
                ],
                "key_terms": [
                    {
                        "kn": "ಮುಚ್ಚಿದ ಮಂಡಲ",
                        "en": "Closed circuit",
                        "meaning_kn": "ಪ್ರವಾಹ ಹರಿಯುವಂತಹ ಪೂರ್ಣ ಮಾರ್ಗ.",
                        "meaning_en": "A complete path that lets current flow.",
                    },
                    {
                        "kn": "ನಿರೋಧಕ",
                        "en": "Insulator",
                        "meaning_kn": "ವಿದ್ಯುತ್ ಸಾಗಿಸದ ಪದಾರ್ಥ.",
                        "meaning_en": "A material that does not carry current.",
                    },
                ],
                "example_en": (
                    "A bicycle dynamo lights its lamp only while the wheel turns, because the "
                    "moving magnet keeps the circuit's charges flowing."
                ),
                "example_kn": (
                    "ಸೈಕಲ್ ಡೈನಮೊ ಚಕ್ರ ತಿರುಗುವಾಗ ಮಾತ್ರ ದೀಪ ಬೆಳಗುತ್ತದೆ; ಏಕೆಂದರೆ "
                    "ಚಲಿಸುವ ಕಾಂತವು ಮಂಡಲದ ಆವೇಶಗಳನ್ನು ಹರಿಯುವಂತೆ ಮಾಡುತ್ತದೆ."
                ),
            },
            {
                "title_en": "Heating effect of electric current",
                "title_kn": "ವಿದ್ಯುತ್ ಪ್ರವಾಹದ ಉಷ್ಣ ಪರಿಣಾಮ",
                "objectives_en": [
                    "Explain why a wire becomes hot when current passes through it.",
                    "Name two appliances that use the heating effect.",
                ],
                "objectives_kn": [
                    "ಪ್ರವಾಹ ಹಾದುಹೋದಾಗ ತಂತಿ ಬಿಸಿಯಾಗುವುದು ಏಕೆ ಎಂಬುದನ್ನು ವಿವರಿಸುವುದು.",
                    "ಉಷ್ಣ ಪರಿಣಾಮ ಬಳಸುವ ಎರಡು ಉಪಕರಣಗಳನ್ನು ಹೆಸರಿಸುವುದು.",
                ],
                "body_en": [
                    "Charges moving through a wire collide with the atoms of the metal and lose "
                    "some energy as heat. A thin, high-resistance wire heats much more than a "
                    "thick copper lead, which is why the element inside an electric kettle glows "
                    "red while the cord stays cool.",
                    "We use this effect on purpose in heaters, irons, toasters, geysers and "
                    "electric stoves, and in the filament of a bulb, which becomes white hot and "
                    "gives light. It is also a nuisance: current in a long wire warms it and "
                    "wastes energy. A fuse protects a circuit by containing a short, thin piece of "
                    "metal that melts and breaks the circuit when the current becomes too large.",
                ],
                "body_kn": [
                    "ತಂತಿಯಲ್ಲಿ ಚಲಿಸುವ ಆವೇಶಗಳು ಲೋಹದ ಪರಮಾಣುಗಳೊಂದಿಗೆ ಘರ್ಷಿಸಿ ಸ್ವಲ್ಪ "
                    "ಶಕ್ತಿಯನ್ನು ಉಷ್ಣವಾಗಿ ಕಳೆದುಕೊಳ್ಳುತ್ತವೆ. ತೆಳುವಾದ, ಹೆಚ್ಚು "
                    "ನಿರೋಧಕತೆಯ ತಂತಿ ದಪ್ಪ ತಾಮ್ರದ ತಂತಿಗಿಂತ ಹೆಚ್ಚು ಬಿಸಿಯಾಗುತ್ತದೆ; "
                    "ಆದ್ದರಿಂದ ವಿದ್ಯುತ್ ಕೆಟಲ್‌ನ ಒಳಗಿನ ಎಳೆ ಕೆಂಪಾಗಿ ಬೆಳಗುತ್ತದೆ, "
                    "ಆದರೆ ತಂತಿ ತಣ್ಣಗಿರುತ್ತದೆ.",
                    "ಈ ಪರಿಣಾಮವನ್ನು ನಾವು ಉದ್ದೇಶಪೂರ್ವಕವಾಗಿ ಹೀಟರ್, ಇಸ್ತ್ರಿ "
                    "ಪೆಟ್ಟಿಗೆ, ಟೋಸ್ಟರ್, ಗೀಸರ್ ಮತ್ತು ವಿದ್ಯುತ್ ಒಲೆಗಳಲ್ಲಿ ಹಾಗೂ "
                    "ಬಲ್ಬ್‌ನ ತಂತುವಿನಲ್ಲಿ ಬಳಸುತ್ತೇವೆ; ಅದು ಬಿಳಿ ಬಿಸಿಯಾಗಿ ಬೆಳಕು "
                    "ನೀಡುತ್ತದೆ. ಇದು ತೊಂದರೆಯೂ ಆಗಬಹುದು: ಉದ್ದ ತಂತಿಯಲ್ಲಿ ಪ್ರವಾಹ "
                    "ಅದನ್ನು ಬೆಚ್ಚಗಾಗಿಸಿ ಶಕ್ತಿ ವ್ಯರ್ಥವಾಗುತ್ತದೆ. ಪ್ರವಾಹ ಬಹಳ "
                    "ಹೆಚ್ಚಾದಾಗ ಕರಗಿ ಮಂಡಲವನ್ನು ಒಡೆಯುವ ಸಣ್ಣ ತೆಳು ಲೋಹದ ತುಣುಕನ್ನು "
                    "ಹೊಂದಿರುವ ಫ್ಯೂಸ್ ಮಂಡಲವನ್ನು ರಕ್ಷಿಸುತ್ತದೆ.",
                ],
                "key_terms": [
                    {
                        "kn": "ನಿರೋಧತೆ",
                        "en": "Resistance",
                        "meaning_kn": "ಪ್ರವಾಹದ ಹರಿವನ್ನು ತಡೆಯುವ ಗುಣ.",
                        "meaning_en": "The property that opposes the flow of current.",
                    },
                    {
                        "kn": "ಫ್ಯೂಸ್",
                        "en": "Fuse",
                        "meaning_kn": "ಅಧಿಕ ಪ್ರವಾಹದಲ್ಲಿ ಕರಗಿ ಮಂಡಲವನ್ನು ರಕ್ಷಿಸುವ ಸಾಧನ.",
                        "meaning_en": "A device that melts to protect a circuit from excess current.",
                    },
                ],
                "example_en": (
                    "An immersion rod heats water in minutes while its own cord stays cool: the "
                    "heating element is designed to resist current, the cord is not."
                ),
                "example_kn": (
                    "ಇಮ್ಮರ್ಶನ್ ರಾಡ್ ನೀರನ್ನು ನಿಮಿಷಗಳಲ್ಲಿ ಕಾಯಿಸುತ್ತದೆ, ಅದರ "
                    "ತಂತಿ ಮಾತ್ರ ತಣ್ಣಗಿರುತ್ತದೆ: ಕಾಯಿಸುವ ಎಳೆಯನ್ನು ಪ್ರವಾಹವನ್ನು "
                    "ತಡೆಯುವಂತೆ ವಿನ್ಯಾಸ ಮಾಡಲಾಗಿದೆ, ತಂತಿಯನ್ನು ಅಲ್ಲ."
                ),
            },
            {
                "title_en": "Magnetic effect of electric current",
                "title_kn": "ವಿದ್ಯುತ್ ಪ್ರವಾಹದ ಕಾಂತೀಯ ಪರಿಣಾಮ",
                "objectives_en": [
                    "Describe the magnetic field around a current-carrying wire.",
                    "Explain how an electromagnet differs from a permanent magnet.",
                ],
                "objectives_kn": [
                    "ಪ್ರವಾಹ ಹರಿಯುವ ತಂತಿಯ ಸುತ್ತ ಇರುವ ಕಾಂತೀಯ ಕ್ಷೇತ್ರವನ್ನು ವಿವರಿಸುವುದು.",
                    "ವಿದ್ಯುತ್ ಕಾಂತ ಮತ್ತು ಶಾಶ್ವತ ಕಾಂತದ ನಡುವಿನ ವ್ಯತ್ಯಾಸವನ್ನು ವಿವರಿಸುವುದು.",
                ],
                "body_en": [
                    "In 1820 a Danish teacher, Hans Christian Oersted, noticed that a compass "
                    "needle twitched whenever he switched on a nearby wire. Current produces a "
                    "magnetic field around itself. Coil the wire around a soft iron nail and the "
                    "field lines line up inside the iron: you have made an electromagnet that "
                    "attracts pins only while the current flows.",
                    "This one idea drives a huge part of modern life. An electric bell uses an "
                    "electromagnet to pull a hammer that strikes a gong, then breaks its own "
                    "circuit so the hammer springs back. A motor uses a coil in a magnetic field to "
                    "turn, powering fans and mixers. In a scrap-yard crane the electromagnet is "
                    "switched on to lift iron and switched off to drop it, which a permanent "
                    "magnet could never do.",
                ],
                "body_kn": [
                    "1820ರಲ್ಲಿ ಡೇನಿಶ್ ಶಿಕ್ಷಕ ಹಾನ್ಸ್ ಕ್ರಿಶ್ಚಿಯನ್ ಓರ್ಸ್ಟೆಡ್, ಬಳಿಯ "
                    "ತಂತಿಯ ಸ್ವಿಚ್ ಆನ್ ಮಾಡಿದಾಗ ಕಾಂಪಾಸ್ ಮುಳ್ಳು ಅಲುಗಾಡುವುದನ್ನು "
                    "ಗಮನಿಸಿದರು. ಪ್ರವಾಹವು ತನ್ನ ಸುತ್ತ ಕಾಂತೀಯ ಕ್ಷೇತ್ರವನ್ನು "
                    "ಉಂಟುಮಾಡುತ್ತದೆ. ತಂತಿಯನ್ನು ಮೆದು ಕಬ್ಬಿಣದ ಮೊಳೆಗೆ ಸುತ್ತಿದರೆ "
                    "ಕ್ಷೇತ್ರ ರೇಖೆಗಳು ಕಬ್ಬಿಣದ ಒಳಗೆ ಜೋಡಣೆಯಾಗುತ್ತವೆ: ಪ್ರವಾಹ "
                    "ಹರಿಯುವಾಗ ಮಾತ್ರ ಪಿನ್‌ಗಳನ್ನು ಆಕರ್ಷಿಸುವ ವಿದ್ಯುತ್ ಕಾಂತ "
                    "ತಯಾರಾಗುತ್ತದೆ.",
                    "ಈ ಒಂದು ಕಲ್ಪನೆಯೇ ಆಧುನಿಕ ಜೀವನದ ದೊಡ್ಡ ಭಾಗವನ್ನು "
                    "ನಡೆಸುತ್ತದೆ. ವಿದ್ಯುತ್ ಗಂಟೆಯಲ್ಲಿ ವಿದ್ಯುತ್ ಕಾಂತವು ಸುತ್ತಿಗೆಯನ್ನು "
                    "ಎಳೆದು ಗಂಟೆಗೆ ಬಡಿಯುತ್ತದೆ, ನಂತರ ತನ್ನದೇ ಮಂಡಲವನ್ನು ಒಡೆದು "
                    "ಸುತ್ತಿಗೆ ಹಿಂತಿರುಗಲು ಬಿಡುತ್ತದೆ. ಮೋಟಾರ್‌ನಲ್ಲಿ ಕಾಂತೀಯ "
                    "ಕ್ಷೇತ್ರದಲ್ಲಿರುವ ಸುರುಳಿ ತಿರುಗಿ ಫ್ಯಾನ್, ಮಿಕ್ಸರ್‌ಗಳನ್ನು "
                    "ನಡೆಸುತ್ತದೆ. ಸ್ಕ್ರ್ಯಾಪ್ ಯಾರ್ಡ್ ಕ್ರೇನ್‌ನಲ್ಲಿ ಕಬ್ಬಿಣವನ್ನು "
                    "ಎತ್ತಲು ವಿದ್ಯುತ್ ಕಾಂತ ಆನ್ ಆಗುತ್ತದೆ, ಬಿಡಲು ಆಫ್ ಆಗುತ್ತದೆ; "
                    "ಶಾಶ್ವತ ಕಾಂತಕ್ಕೆ ಇದು ಸಾಧ್ಯವಿಲ್ಲ.",
                ],
                "key_terms": [
                    {
                        "kn": "ವಿದ್ಯುತ್ ಕಾಂತ",
                        "en": "Electromagnet",
                        "meaning_kn": "ಪ್ರವಾಹ ಹರಿಯುವಾಗ ಮಾತ್ರ ಕಾಂತವಾಗುವ ಸುರುಳಿ.",
                        "meaning_en": "A coil that acts as a magnet only while current flows.",
                    },
                    {
                        "kn": "ಕಾಂತೀಯ ಕ್ಷೇತ್ರ",
                        "en": "Magnetic field",
                        "meaning_kn": "ಕಾಂತದ ಸುತ್ತ ಪ್ರಭಾವ ಇರುವ ಪ್ರದೇಶ.",
                        "meaning_en": "The region around a magnet where its effect is felt.",
                    },
                ],
                "example_en": (
                    "A doorbell rings in short bursts because its own electromagnet keeps "
                    "switching the circuit off and on many times a second."
                ),
                "example_kn": (
                    "ಬಾಗಿಲ ಗಂಟೆ ಸಣ್ಣ ಸಣ್ಣ ಸ್ಫೋಟಗಳಂತೆ ಬಡಿಯುವುದು ಏಕೆಂದರೆ ಅದರ "
                    "ವಿದ್ಯುತ್ ಕಾಂತವೇ ಸೆಕೆಂಡಿಗೆ ಅನೇಕ ಬಾರಿ ಮಂಡಲವನ್ನು "
                    "ಆಫ್-ಆನ್ ಮಾಡುತ್ತದೆ."
                ),
            },
        ],
        "notes_en": [
            "Current flows only in a closed circuit; opening the switch breaks the path.",
            "Metals conduct; plastic and rubber insulate. Use cells, never mains, in class.",
            "Moving charges heat the wire they pass through: the heating effect.",
            "Heaters, irons, geysers and bulb filaments use the heating effect.",
            "A fuse melts and breaks the circuit when the current is too large.",
            "Current creates a magnetic field; a coil around soft iron makes an electromagnet.",
            "Bells, motors and cranes use the magnetic effect.",
        ],
        "notes_kn": [
            "ಪ್ರವಾಹ ಮುಚ್ಚಿದ ಮಂಡಲದಲ್ಲಿ ಮಾತ್ರ ಹರಿಯುತ್ತದೆ; ಸ್ವಿಚ್ ತೆರೆದರೆ ಮಾರ್ಗ ಒಡೆಯುತ್ತದೆ.",
            "ಲೋಹಗಳು ವಾಹಕಗಳು; ಪ್ಲಾಸ್ಟಿಕ್ ಮತ್ತು ರಬ್ಬರ್ ನಿರೋಧಕಗಳು. ತರಗತಿಯಲ್ಲಿ ಕೋಶಗಳನ್ನೇ ಬಳಸಿ, ಮುಖ್ಯ ವಿದ್ಯುತ್ ಎಂದೂ ಬೇಡ.",
            "ಚಲಿಸುವ ಆವೇಶಗಳು ತಾವು ಹಾದುಹೋಗುವ ತಂತಿಯನ್ನು ಬಿಸಿ ಮಾಡುತ್ತವೆ: ಉಷ್ಣ ಪರಿಣಾಮ.",
            "ಹೀಟರ್, ಇಸ್ತ್ರಿ, ಗೀಸರ್ ಮತ್ತು ಬಲ್ಬ್ ತಂತು ಉಷ್ಣ ಪರಿಣಾಮ ಬಳಸುತ್ತವೆ.",
            "ಪ್ರವಾಹ ಬಹಳ ಹೆಚ್ಚಾದಾಗ ಫ್ಯೂಸ್ ಕರಗಿ ಮಂಡಲವನ್ನು ಒಡೆಯುತ್ತದೆ.",
            "ಪ್ರವಾಹ ಕಾಂತೀಯ ಕ್ಷೇತ್ರ ಉಂಟುಮಾಡುತ್ತದೆ; ಮೆದು ಕಬ್ಬಿಣದ ಸುತ್ತ ಸುರುಳಿ ವಿದ್ಯುತ್ ಕಾಂತವಾಗುತ್ತದೆ.",
            "ಗಂಟೆ, ಮೋಟಾರ್ ಮತ್ತು ಕ್ರೇನ್ ಕಾಂತೀಯ ಪರಿಣಾಮ ಬಳಸುತ್ತವೆ.",
        ],
        "videos": [
            {
                "title": "ವಿದ್ಯುತ್ ಪ್ರವಾಹದ ಪರಿಣಾಮಗಳು — ಕನ್ನಡ",
                "language": "kn",
                "topic": "Electric current",
                "search_query": "ವಿದ್ಯುತ್ ಪ್ರವಾಹ ಉಷ್ಣ ಕಾಂತೀಯ ಪರಿಣಾಮ ಕನ್ನಡ 8ನೇ ತರಗತಿ",
            },
            {
                "title": "Electric current: heating and magnetic effects",
                "language": "en",
                "topic": "Electric current",
                "search_query": "heating and magnetic effect of electric current class 8 science",
            },
        ],
        "quiz": [
            {
                "question_en": "A bulb glows only when…",
                "question_kn": "ಬಲ್ಬ್ ಬೆಳಗುವುದು ಯಾವಾಗ ಮಾತ್ರ?",
                "options_en": [
                    "the switch is open",
                    "the circuit is closed and complete",
                    "the cell is removed",
                    "the wire is made of plastic",
                ],
                "options_kn": [
                    "ಸ್ವಿಚ್ ತೆರೆದಿದ್ದಾಗ",
                    "ಮಂಡಲ ಮುಚ್ಚಿ ಪೂರ್ಣವಾಗಿದ್ದಾಗ",
                    "ಕೋಶವನ್ನು ತೆಗೆದಾಗ",
                    "ತಂತಿ ಪ್ಲಾಸ್ಟಿಕ್‌ನದ್ದಾಗಿದ್ದಾಗ",
                ],
                "correct_index": 1,
                "explanation_en": (
                    "Current needs an unbroken path. Opening the switch breaks that path, so "
                    "charges stop moving and the bulb goes dark."
                ),
                "explanation_kn": (
                    "ಪ್ರವಾಹಕ್ಕೆ ಕಡಿತವಿಲ್ಲದ ಮಾರ್ಗ ಬೇಕು. ಸ್ವಿಚ್ ತೆರೆದರೆ ಆ ಮಾರ್ಗ "
                    "ಒಡೆಯುತ್ತದೆ; ಆವೇಶಗಳ ಚಲನೆ ನಿಂತು ಬಲ್ಬ್ ಆರಿಹೋಗುತ್ತದೆ."
                ),
                "difficulty": 1,
            },
            {
                "question_en": "An electric iron works because of the…",
                "question_kn": "ವಿದ್ಯುತ್ ಇಸ್ತ್ರಿ ಪೆಟ್ಟಿಗೆ ಯಾವ ಪರಿಣಾಮದಿಂದ ಕೆಲಸ ಮಾಡುತ್ತದೆ?",
                "options_en": [
                    "magnetic effect",
                    "chemical effect",
                    "heating effect",
                    "cooling effect",
                ],
                "options_kn": [
                    "ಕಾಂತೀಯ ಪರಿಣಾಮ",
                    "ರಾಸಾಯನಿಕ ಪರಿಣಾಮ",
                    "ಉಷ್ಣ ಪರಿಣಾಮ",
                    "ತಣ್ಣಗಾಗುವ ಪರಿಣಾಮ",
                ],
                "correct_index": 2,
                "explanation_en": (
                    "The element inside an iron is a high-resistance wire. Current through it "
                    "produces heat, and that heat presses the cloth smooth."
                ),
                "explanation_kn": (
                    "ಇಸ್ತ್ರಿಯ ಒಳಗಿನ ಎಳೆ ಹೆಚ್ಚು ನಿರೋಧಕತೆಯ ತಂತಿ. ಅದರ ಮೂಲಕ "
                    "ಹರಿಯುವ ಪ್ರವಾಹ ಉಷ್ಣ ಉಂಟುಮಾಡುತ್ತದೆ; ಆ ಉಷ್ಣ ಬಟ್ಟೆಯನ್ನು "
                    "ನಯವಾಗಿಸುತ್ತದೆ."
                ),
                "difficulty": 1,
            },
            {
                "question_en": "What happens when current flows through a wire coiled around a soft iron nail?",
                "question_kn": "ಮೆದು ಕಬ್ಬಿಣದ ಮೊಳೆಗೆ ಸುತ್ತಿದ ತಂತಿಯಲ್ಲಿ ಪ್ರವಾಹ ಹರಿದಾಗ ಏನಾಗುತ್ತದೆ?",
                "options_en": [
                    "The nail melts",
                    "The nail becomes a magnet while current flows",
                    "The nail turns into copper",
                    "Nothing at all happens",
                ],
                "options_kn": [
                    "ಮೊಳೆ ಕರಗುತ್ತದೆ",
                    "ಪ್ರವಾಹ ಹರಿಯುವವರೆಗೆ ಮೊಳೆ ಕಾಂತವಾಗುತ್ತದೆ",
                    "ಮೊಳೆ ತಾಮ್ರವಾಗಿ ಬದಲಾಗುತ್ತದೆ",
                    "ಏನೂ ಆಗುವುದಿಲ್ಲ",
                ],
                "correct_index": 1,
                "explanation_en": (
                    "This is an electromagnet. Its magnetism lasts only while the current flows, "
                    "which is exactly what a bell or a crane needs."
                ),
                "explanation_kn": (
                    "ಇದೇ ವಿದ್ಯುತ್ ಕಾಂತ. ಪ್ರವಾಹ ಹರಿಯುವವರೆಗೆ ಮಾತ್ರ ಕಾಂತತ್ವ "
                    "ಇರುತ್ತದೆ; ಗಂಟೆ ಅಥವಾ ಕ್ರೇನ್‌ಗೆ ಬೇಕಾಗಿರುವುದೂ ಇದೇ."
                ),
                "difficulty": 2,
            },
            {
                "question_en": "What is the job of a fuse in a circuit?",
                "question_kn": "ಮಂಡಲದಲ್ಲಿ ಫ್ಯೂಸ್‌ನ ಕೆಲಸ ಏನು?",
                "options_en": [
                    "To make the bulb brighter",
                    "To store electricity for later",
                    "To melt and break the circuit when current is too high",
                    "To convert current into magnetism only",
                ],
                "options_kn": [
                    "ಬಲ್ಬ್ ಹೆಚ್ಚು ಬೆಳಗಿಸುವುದು",
                    "ವಿದ್ಯುತ್ತನ್ನು ಸಂಗ್ರಹಿಸಿಡುವುದು",
                    "ಪ್ರವಾಹ ಬಹಳ ಹೆಚ್ಚಾದಾಗ ಕರಗಿ ಮಂಡಲವನ್ನು ಒಡೆಯುವುದು",
                    "ಪ್ರವಾಹವನ್ನು ಕಾಂತತ್ವವಾಗಿ ಮಾತ್ರ ಬದಲಿಸುವುದು",
                ],
                "correct_index": 2,
                "explanation_en": (
                    "A fuse is a deliberate weak point. Too much current melts it, which stops "
                    "the current before wiring or appliances are damaged."
                ),
                "explanation_kn": (
                    "ಫ್ಯೂಸ್ ಉದ್ದೇಶಪೂರ್ವಕವಾಗಿ ಇಟ್ಟ ದುರ್ಬಲ ಸ್ಥಾನ. ಅಧಿಕ ಪ್ರವಾಹ "
                    "ಅದನ್ನು ಕರಗಿಸಿ, ತಂತಿ ಅಥವಾ ಉಪಕರಣ ಹಾಳಾಗುವ ಮೊದಲೇ ಪ್ರವಾಹವನ್ನು "
                    "ನಿಲ್ಲಿಸುತ್ತದೆ."
                ),
                "difficulty": 2,
            },
            {
                "question_en": "Why is an electromagnet better than a permanent magnet in a scrap crane?",
                "question_kn": "ಸ್ಕ್ರ್ಯಾಪ್ ಕ್ರೇನ್‌ನಲ್ಲಿ ವಿದ್ಯುತ್ ಕಾಂತ ಶಾಶ್ವತ ಕಾಂತಕ್ಕಿಂತ ಉತ್ತಮ ಏಕೆ?",
                "options_en": [
                    "It is cheaper to paint",
                    "It can be switched off to release the iron",
                    "It works without any current",
                    "It attracts plastic too",
                ],
                "options_kn": [
                    "ಬಣ್ಣ ಹಾಕಲು ಅಗ್ಗ",
                    "ಕಬ್ಬಿಣವನ್ನು ಬಿಡಲು ಅದನ್ನು ಆಫ್ ಮಾಡಬಹುದು",
                    "ಪ್ರವಾಹ ಇಲ್ಲದೆಯೂ ಕೆಲಸ ಮಾಡುತ್ತದೆ",
                    "ಪ್ಲಾಸ್ಟಿಕ್ ಅನ್ನೂ ಆಕರ್ಷಿಸುತ್ತದೆ",
                ],
                "correct_index": 1,
                "explanation_en": (
                    "A permanent magnet would hold the load forever. An electromagnet releases it "
                    "the moment the current is switched off."
                ),
                "explanation_kn": (
                    "ಶಾಶ್ವತ ಕಾಂತವು ಭಾರವನ್ನು ಶಾಶ್ವತವಾಗಿ ಹಿಡಿದಿಡುತ್ತಿತ್ತು. "
                    "ವಿದ್ಯುತ್ ಕಾಂತವನ್ನು ಆಫ್ ಮಾಡಿದ ಕ್ಷಣ ಅದು ಭಾರವನ್ನು "
                    "ಬಿಡುಗಡೆ ಮಾಡುತ್ತದೆ."
                ),
                "difficulty": 3,
            },
        ],
    },
    {
        "number": 4,
        "category": "physics",
        "is_enrichment": False,
        "title_en": "Exploring Forces",
        "title_kn": "ಬಲಗಳ ಅನ್ವೇಷಣೆ",
        "summary_en": (
            "A push, a pull, a rub or the Earth itself: learn what a force is, how friction "
            "helps and hinders us, and why gravity keeps everything on the ground."
        ),
        "summary_kn": (
            "ತಳ್ಳುವಿಕೆ, ಎಳೆಯುವಿಕೆ, ಉಜ್ಜುವಿಕೆ ಅಥವಾ ಭೂಮಿಯೇ: ಬಲ ಎಂದರೇನು, ಘರ್ಷಣೆ "
            "ಹೇಗೆ ಸಹಾಯ ಮತ್ತು ತೊಂದರೆ ಮಾಡುತ್ತದೆ, ಮತ್ತು ಗುರುತ್ವ ಎಲ್ಲವನ್ನೂ "
            "ನೆಲದ ಮೇಲೆ ಏಕೆ ಇಡುತ್ತದೆ ಎಂಬುದನ್ನು ಕಲಿಯಿರಿ."
        ),
        "estimated_minutes": 40,
        "visualizations": ["forces"],
        "topics": [
            {
                "title_en": "What is a force?",
                "title_kn": "ಬಲ ಎಂದರೇನು?",
                "objectives_en": [
                    "Define force and give push and pull examples.",
                    "Explain how a force can change speed, direction or shape.",
                ],
                "objectives_kn": [
                    "ಬಲವನ್ನು ವ್ಯಾಖ್ಯಾನಿಸಿ ತಳ್ಳುವಿಕೆ ಮತ್ತು ಎಳೆಯುವಿಕೆಯ ಉದಾಹರಣೆಗಳನ್ನು ನೀಡುವುದು.",
                    "ಬಲವು ವೇಗ, ದಿಕ್ಕು ಅಥವಾ ಆಕಾರವನ್ನು ಹೇಗೆ ಬದಲಿಸಬಲ್ಲದು ಎಂಬುದನ್ನು ವಿವರಿಸುವುದು.",
                ],
                "body_en": [
                    "A force is a push or a pull acting on an object. You push a door, pull a "
                    "drawer, squeeze a lemon and kick a ball. Force has both size and direction, "
                    "so 'ten newtons to the right' is a complete description while 'ten newtons' "
                    "is not. Two forces acting in opposite directions partly cancel each other.",
                    "A force can start an object moving, slow it down, stop it, change its "
                    "direction, or change its shape. A goalkeeper stops a ball, a batsman changes "
                    "its direction, and a potter changes the shape of clay. When the forces on an "
                    "object balance, its motion does not change: a book resting on a table stays "
                    "still because its weight is balanced by the table's upward push.",
                ],
                "body_kn": [
                    "ಬಲ ಎಂದರೆ ವಸ್ತುವಿನ ಮೇಲೆ ಆಗುವ ತಳ್ಳುವಿಕೆ ಅಥವಾ ಎಳೆಯುವಿಕೆ. ನೀವು "
                    "ಬಾಗಿಲನ್ನು ತಳ್ಳುತ್ತೀರಿ, ಸೆಳೆಖಾನೆಯನ್ನು ಎಳೆಯುತ್ತೀರಿ, ನಿಂಬೆ "
                    "ಹಿಂಡುತ್ತೀರಿ ಮತ್ತು ಚೆಂಡನ್ನು ಒದೆಯುತ್ತೀರಿ. ಬಲಕ್ಕೆ ಗಾತ್ರ ಮತ್ತು "
                    "ದಿಕ್ಕು ಎರಡೂ ಇರುತ್ತವೆ; ಆದ್ದರಿಂದ 'ಬಲಕ್ಕೆ ಹತ್ತು ನ್ಯೂಟನ್' ಪೂರ್ಣ "
                    "ವಿವರಣೆ, 'ಹತ್ತು ನ್ಯೂಟನ್' ಅಲ್ಲ. ವಿರುದ್ಧ ದಿಕ್ಕಿನಲ್ಲಿ "
                    "ಕೆಲಸ ಮಾಡುವ ಎರಡು ಬಲಗಳು ಸ್ವಲ್ಪಮಟ್ಟಿಗೆ ಪರಸ್ಪರ ರದ್ದಾಗುತ್ತವೆ.",
                    "ಬಲವು ವಸ್ತುವನ್ನು ಚಲಿಸಲು ಪ್ರಾರಂಭಿಸಬಹುದು, ನಿಧಾನಗೊಳಿಸಬಹುದು, "
                    "ನಿಲ್ಲಿಸಬಹುದು, ಅದರ ದಿಕ್ಕನ್ನು ಬದಲಿಸಬಹುದು ಅಥವಾ ಆಕಾರವನ್ನು "
                    "ಬದಲಿಸಬಹುದು. ಗೋಲ್‌ಕೀಪರ್ ಚೆಂಡನ್ನು ನಿಲ್ಲಿಸುತ್ತಾನೆ, ಬ್ಯಾಟ್ಸ್‌ಮನ್ "
                    "ಅದರ ದಿಕ್ಕನ್ನು ಬದಲಿಸುತ್ತಾನೆ, ಕುಂಬಾರ ಜೇಡಿಮಣ್ಣಿನ ಆಕಾರ "
                    "ಬದಲಿಸುತ್ತಾನೆ. ವಸ್ತುವಿನ ಮೇಲಿನ ಬಲಗಳು ಸಮತೋಲನದಲ್ಲಿದ್ದರೆ ಚಲನೆ "
                    "ಬದಲಾಗುವುದಿಲ್ಲ: ಮೇಜಿನ ಮೇಲಿರುವ ಪುಸ್ತಕ ಸ್ಥಿರವಾಗಿರುವುದು ಅದರ "
                    "ತೂಕವನ್ನು ಮೇಜಿನ ಮೇಲ್ಮುಖ ತಳ್ಳುವಿಕೆ ಸರಿದೂಗಿಸುವುದರಿಂದ."
                ],
                "key_terms": [
                    {
                        "kn": "ಬಲ",
                        "en": "Force",
                        "meaning_kn": "ವಸ್ತುವಿನ ಚಲನೆ ಅಥವಾ ಆಕಾರ ಬದಲಿಸುವ ತಳ್ಳುವಿಕೆ/ಎಳೆಯುವಿಕೆ.",
                        "meaning_en": "A push or pull that can change motion or shape.",
                    },
                    {
                        "kn": "ಸಮತೋಲಿತ ಬಲಗಳು",
                        "en": "Balanced forces",
                        "meaning_kn": "ಪರಸ್ಪರ ಸರಿದೂಗಿಸುವ ಸಮಾನ ಮತ್ತು ವಿರುದ್ಧ ಬಲಗಳು.",
                        "meaning_en": "Equal, opposite forces that cancel each other.",
                    },
                ],
                "example_en": (
                    "Tug-of-war with equal teams ends in a stalemate: both sides pull hard, but "
                    "the rope does not move."
                ),
                "example_kn": (
                    "ಸಮಾನ ಶಕ್ತಿಯ ಎರಡು ತಂಡಗಳ ಹಗ್ಗಜಗ್ಗಾಟ ಸಮನಾಗಿ ಮುಗಿಯುತ್ತದೆ: "
                    "ಇಬ್ಬರೂ ಬಲವಾಗಿ ಎಳೆಯುತ್ತಾರೆ, ಆದರೆ ಹಗ್ಗ ಚಲಿಸುವುದಿಲ್ಲ."
                ),
            },
            {
                "title_en": "Friction",
                "title_kn": "ಘರ್ಷಣೆ",
                "objectives_en": [
                    "Explain why friction opposes sliding motion.",
                    "Give one case where friction helps and one where it is a problem.",
                ],
                "objectives_kn": [
                    "ಘರ್ಷಣೆ ಜಾರುವ ಚಲನೆಯನ್ನು ಏಕೆ ವಿರೋಧಿಸುತ್ತದೆ ಎಂಬುದನ್ನು ವಿವರಿಸುವುದು.",
                    "ಘರ್ಷಣೆ ಸಹಾಯ ಮಾಡುವ ಮತ್ತು ತೊಂದರೆ ಕೊಡುವ ಒಂದೊಂದು ಸಂದರ್ಭವನ್ನು ಹೇಳುವುದು.",
                ],
                "body_en": [
                    "Even apparently smooth surfaces are rough when magnified. When one surface "
                    "slides over another, tiny bumps catch on each other, and this opposition is "
                    "called friction. Friction acts along the surface, always against the "
                    "direction of sliding, and it produces heat.",
                    "Friction is useful: without it we could not walk, a bicycle brake would do "
                    "nothing, and a knot would slip open. It is also wasteful: it wears out shoe "
                    "soles, heats machine parts and makes heavy boxes hard to push. We reduce it "
                    "with oil or grease (lubricants), with ball bearings, and by making surfaces "
                    "smoother. We increase it with rough treads on tyres, grooves in soles and "
                    "sand on an icy path.",
                ],
                "body_kn": [
                    "ನಯವಾಗಿ ಕಾಣುವ ಮೇಲ್ಮೈಗಳೂ ಸಹ ವರ್ಧಿಸಿ ನೋಡಿದಾಗ ಒರಟಾಗಿರುತ್ತವೆ. "
                    "ಒಂದು ಮೇಲ್ಮೈ ಇನ್ನೊಂದರ ಮೇಲೆ ಜಾರಿದಾಗ ಸಣ್ಣ ಉಬ್ಬುಗಳು "
                    "ಪರಸ್ಪರ ಸಿಕ್ಕಿಕೊಳ್ಳುತ್ತವೆ; ಈ ವಿರೋಧವನ್ನೇ ಘರ್ಷಣೆ ಎನ್ನುತ್ತೇವೆ. "
                    "ಘರ್ಷಣೆ ಮೇಲ್ಮೈಯ ಉದ್ದಕ್ಕೂ, ಯಾವಾಗಲೂ ಜಾರುವಿಕೆಯ ವಿರುದ್ಧ "
                    "ದಿಕ್ಕಿನಲ್ಲಿ ಕೆಲಸ ಮಾಡುತ್ತದೆ ಮತ್ತು ಉಷ್ಣ ಉಂಟುಮಾಡುತ್ತದೆ.",
                    "ಘರ್ಷಣೆ ಉಪಯುಕ್ತ: ಅದಿಲ್ಲದಿದ್ದರೆ ನಡೆಯಲು ಸಾಧ್ಯವಿಲ್ಲ, ಸೈಕಲ್ "
                    "ಬ್ರೇಕ್ ಏನೂ ಮಾಡುತ್ತಿರಲಿಲ್ಲ, ಗಂಟು ಸಡಿಲವಾಗಿ ಬಿಚ್ಚಿಹೋಗುತ್ತಿತ್ತು. "
                    "ಅದೇ ಸಮಯದಲ್ಲಿ ವ್ಯರ್ಥವೂ ಹೌದು: ಶೂನ ಅಟ್ಟೆ ಸವೆಯುತ್ತದೆ, "
                    "ಯಂತ್ರಭಾಗಗಳು ಬಿಸಿಯಾಗುತ್ತವೆ, ಭಾರವಾದ ಪೆಟ್ಟಿಗೆಗಳನ್ನು "
                    "ತಳ್ಳುವುದು ಕಷ್ಟವಾಗುತ್ತದೆ. ಎಣ್ಣೆ ಅಥವಾ ಗ್ರೀಸ್ (ಸ್ನೇಗಕಗಳು), "
                    "ಬಾಲ್ ಬೇರಿಂಗ್ ಮತ್ತು ಮೇಲ್ಮೈಗಳನ್ನು ನಯಗೊಳಿಸುವುದರಿಂದ ಘರ್ಷಣೆ "
                    "ಕಡಿಮೆ ಮಾಡುತ್ತೇವೆ. ಟೈರಿನ ಒರಟು ಚಕ್ರ, ಶೂನ ಅಟ್ಟೆಯ ಚಾಲುಗಳು "
                    "ಮತ್ತು ಮಂಜಿನ ದಾರಿಯಲ್ಲಿ ಮರಳು ಹಾಕುವುದರಿಂದ ಘರ್ಷಣೆ "
                    "ಹೆಚ್ಚಿಸುತ್ತೇವೆ.",
                ],
                "key_terms": [
                    {
                        "kn": "ಘರ್ಷಣೆ",
                        "en": "Friction",
                        "meaning_kn": "ಎರಡು ಮೇಲ್ಮೈಗಳ ನಡುವೆ ಚಲನೆಯನ್ನು ವಿರೋಧಿಸುವ ಬಲ.",
                        "meaning_en": "A force between two surfaces that opposes sliding.",
                    },
                    {
                        "kn": "ಸ್ನೇಗಕ",
                        "en": "Lubricant",
                        "meaning_kn": "ಘರ್ಷಣೆ ಕಡಿಮೆ ಮಾಡಲು ಬಳಸುವ ಎಣ್ಣೆ ಅಥವಾ ಕೊಬ್ಬು.",
                        "meaning_en": "An oil or grease used to reduce friction.",
                    },
                ],
                "example_en": (
                    "Rubbing your palms together warms them: friction turns motion into heat, "
                    "exactly as a bicycle brake pad heats its rim."
                ),
                "example_kn": (
                    "ಅಂಗೈಗಳನ್ನು ಉಜ್ಜಿದಾಗ ಬೆಚ್ಚಗಾಗುತ್ತವೆ: ಘರ್ಷಣೆ ಚಲನೆಯನ್ನು "
                    "ಉಷ್ಣವಾಗಿ ಬದಲಿಸುತ್ತದೆ; ಸೈಕಲ್ ಬ್ರೇಕ್ ಪ್ಯಾಡ್ ಚಕ್ರದ "
                    "ಅಂಚನ್ನು ಬಿಸಿ ಮಾಡುವಂತೆಯೇ."
                ),
            },
            {
                "title_en": "Gravity",
                "title_kn": "ಗುರುತ್ವ",
                "objectives_en": [
                    "Explain that gravity is a pull towards the Earth's centre.",
                    "Describe why weight differs from mass.",
                ],
                "objectives_kn": [
                    "ಗುರುತ್ವವು ಭೂಮಿಯ ಕೇಂದ್ರದ ಕಡೆಗಿನ ಎಳೆಯುವಿಕೆ ಎಂದು ವಿವರಿಸುವುದು.",
                    "ತೂಕ ಮತ್ತು ರಾಶಿ ಏಕೆ ಬೇರೆ ಎಂಬುದನ್ನು ವಿವರಿಸುವುದು.",
                ],
                "body_en": [
                    "Every object with mass pulls every other object. The Earth is enormous, so "
                    "its pull dominates our daily life: we call it gravity. It always acts towards "
                    "the centre of the Earth, which is why a dropped stone falls straight down and "
                    "why a ball thrown up slows, stops and returns.",
                    "Gravity also explains why water flows downhill, why a mango falls from a "
                    "tree, and why the Moon stays in orbit instead of flying away. Mass is the "
                    "amount of matter in a body and does not change; weight is the pull of gravity "
                    "on that mass and does change. Your mass is the same on the Moon, but your "
                    "weight there is about one-sixth as much because the Moon is far less massive.",
                ],
                "body_kn": [
                    "ರಾಶಿ ಇರುವ ಪ್ರತಿ ವಸ್ತುವೂ ಇತರ ವಸ್ತುಗಳನ್ನು ಎಳೆಯುತ್ತದೆ. ಭೂಮಿ "
                    "ಬಹಳ ದೊಡ್ಡದಾದ್ದರಿಂದ ಅದರ ಎಳೆಯುವಿಕೆಯೇ ನಮ್ಮ ದಿನನಿತ್ಯದ "
                    "ಜೀವನದಲ್ಲಿ ಪ್ರಧಾನ: ಅದನ್ನೇ ಗುರುತ್ವ ಎನ್ನುತ್ತೇವೆ. ಅದು ಯಾವಾಗಲೂ "
                    "ಭೂಮಿಯ ಕೇಂದ್ರದ ಕಡೆಗೆ ಕೆಲಸ ಮಾಡುತ್ತದೆ; ಆದ್ದರಿಂದ ಬಿಟ್ಟ ಕಲ್ಲು "
                    "ನೇರವಾಗಿ ಕೆಳಗೆ ಬೀಳುತ್ತದೆ, ಮೇಲಕ್ಕೆ ಎಸೆದ ಚೆಂಡು ನಿಧಾನವಾಗಿ ನಿಂತು "
                    "ಮರಳಿ ಬರುತ್ತದೆ.",
                    "ನೀರು ಇಳಿಜಾರಿನಲ್ಲಿ ಹರಿಯುವುದು, ಮರದಿಂದ ಮಾವು ಬೀಳುವುದು "
                    "ಮತ್ತು ಚಂದ್ರನು ಹಾರಿಹೋಗದೆ ಕಕ್ಷೆಯಲ್ಲಿ ಉಳಿಯುವುದು ಇವೆಲ್ಲವನ್ನೂ "
                    "ಗುರುತ್ವ ವಿವರಿಸುತ್ತದೆ. ರಾಶಿ ಎಂದರೆ ದೇಹದಲ್ಲಿರುವ ಪದಾರ್ಥದ "
                    "ಪ್ರಮಾಣ; ಅದು ಬದಲಾಗುವುದಿಲ್ಲ. ತೂಕ ಎಂದರೆ ಆ ರಾಶಿಯ ಮೇಲೆ "
                    "ಗುರುತ್ವದ ಎಳೆಯುವಿಕೆ; ಅದು ಬದಲಾಗುತ್ತದೆ. ಚಂದ್ರನ ಮೇಲೂ ನಿಮ್ಮ "
                    "ರಾಶಿ ಅಷ್ಟೇ, ಆದರೆ ಚಂದ್ರನ ರಾಶಿ ಬಹಳ ಕಡಿಮೆಯಾದ್ದರಿಂದ ಅಲ್ಲಿ "
                    "ನಿಮ್ಮ ತೂಕ ಸುಮಾರು ಆರರಲ್ಲಿ ಒಂದು ಭಾಗ ಮಾತ್ರ."
                ],
                "key_terms": [
                    {
                        "kn": "ಗುರುತ್ವ",
                        "en": "Gravity",
                        "meaning_kn": "ಭೂಮಿ ವಸ್ತುಗಳನ್ನು ತನ್ನ ಕೇಂದ್ರದ ಕಡೆಗೆ ಎಳೆಯುವ ಬಲ.",
                        "meaning_en": "The pull of the Earth towards its centre.",
                    },
                    {
                        "kn": "ರಾಶಿ",
                        "en": "Mass",
                        "meaning_kn": "ದೇಹದಲ್ಲಿರುವ ಪದಾರ್ಥದ ಪ್ರಮಾಣ, ಬದಲಾಗದುದು.",
                        "meaning_en": "The amount of matter in a body; it does not change.",
                    },
                ],
                "example_en": (
                    "A coin and a crumpled paper ball dropped together land almost together, "
                    "because gravity pulls both down at the same rate."
                ),
                "example_kn": (
                    "ಒಂದೇ ಸಮಯದಲ್ಲಿ ಬಿಟ್ಟ ನಾಣ್ಯ ಮತ್ತು ಚಪ್ಪಟೆ ಮಾಡಿದ ಕಾಗದದ "
                    "ಚೆಂಡು ಬಹುತೇಕ ಒಟ್ಟಿಗೇ ನೆಲಕ್ಕೆ ಬೀಳುತ್ತವೆ; ಏಕೆಂದರೆ "
                    "ಗುರುತ್ವ ಎರಡನ್ನೂ ಒಂದೇ ದರದಲ್ಲಿ ಕೆಳಗೆ ಎಳೆಯುತ್ತದೆ."
                ),
            },
        ],
        "notes_en": [
            "A force is a push or a pull; it has size and direction.",
            "Forces can start, stop, slow, turn or reshape an object.",
            "Balanced forces leave motion unchanged.",
            "Friction opposes sliding and produces heat.",
            "Lubricants, bearings and smooth surfaces reduce friction; treads and roughness increase it.",
            "Gravity pulls every mass towards the Earth's centre.",
            "Mass is constant; weight depends on the pull of gravity.",
        ],
        "notes_kn": [
            "ಬಲ ಎಂದರೆ ತಳ್ಳುವಿಕೆ ಅಥವಾ ಎಳೆಯುವಿಕೆ; ಅದಕ್ಕೆ ಗಾತ್ರ ಮತ್ತು ದಿಕ್ಕು ಇರುತ್ತವೆ.",
            "ಬಲಗಳು ವಸ್ತುವನ್ನು ಚಲಿಸಲು ಪ್ರಾರಂಭಿಸಬಹುದು, ನಿಲ್ಲಿಸಬಹುದು, ನಿಧಾನಗೊಳಿಸಬಹುದು, ತಿರುಗಿಸಬಹುದು ಅಥವಾ ಆಕಾರ ಬದಲಿಸಬಹುದು.",
            "ಸಮತೋಲಿತ ಬಲಗಳಿದ್ದರೆ ಚಲನೆ ಬದಲಾಗುವುದಿಲ್ಲ.",
            "ಘರ್ಷಣೆ ಜಾರುವಿಕೆಯನ್ನು ವಿರೋಧಿಸಿ ಉಷ್ಣ ಉಂಟುಮಾಡುತ್ತದೆ.",
            "ಸ್ನೇಗಕ, ಬೇರಿಂಗ್ ಮತ್ತು ನಯ ಮೇಲ್ಮೈ ಘರ್ಷಣೆ ಕಡಿಮೆ ಮಾಡುತ್ತವೆ; ಚಕ್ರದ ಚಾಲು ಮತ್ತು ಒರಟುತನ ಹೆಚ್ಚಿಸುತ್ತವೆ.",
            "ಗುರುತ್ವ ಪ್ರತಿ ರಾಶಿಯನ್ನೂ ಭೂಮಿಯ ಕೇಂದ್ರದ ಕಡೆಗೆ ಎಳೆಯುತ್ತದೆ.",
            "ರಾಶಿ ಸ್ಥಿರ; ತೂಕ ಗುರುತ್ವದ ಎಳೆಯುವಿಕೆಯನ್ನು ಅವಲಂಬಿಸಿದೆ.",
        ],
        "videos": [
            {
                "title": "ಬಲ ಮತ್ತು ಘರ್ಷಣೆ — ಕನ್ನಡ ಪಾಠ",
                "language": "kn",
                "topic": "Forces and friction",
                "search_query": "ಬಲ ಘರ್ಷಣೆ ಗುರುತ್ವ ಕನ್ನಡ 8ನೇ ತರಗತಿ ವಿಜ್ಞಾನ",
            },
            {
                "title": "Force, friction and gravity for Class 8",
                "language": "en",
                "topic": "Forces and friction",
                "search_query": "force friction gravity class 8 science explained",
            },
        ],
        "quiz": [
            {
                "question_en": "Which of these is NOT a force?",
                "question_kn": "ಇವುಗಳಲ್ಲಿ ಬಲ ಅಲ್ಲದಿರುವುದು ಯಾವುದು?",
                "options_en": ["A push on a door", "A pull on a rope", "The mass of a stone", "Friction on a slide"],
                "options_kn": ["ಬಾಗಿಲಿನ ಮೇಲಿನ ತಳ್ಳುವಿಕೆ", "ಹಗ್ಗದ ಮೇಲಿನ ಎಳೆಯುವಿಕೆ", "ಕಲ್ಲಿನ ರಾಶಿ", "ಜಾರುಬಂಡಿಯ ಮೇಲಿನ ಘರ್ಷಣೆ"],
                "correct_index": 2,
                "explanation_en": (
                    "Mass is a measure of matter, not a push or pull. The other three are forces "
                    "acting on objects."
                ),
                "explanation_kn": (
                    "ರಾಶಿ ಎಂದರೆ ಪದಾರ್ಥದ ಪ್ರಮಾಣ, ತಳ್ಳುವಿಕೆ ಅಥವಾ ಎಳೆಯುವಿಕೆ ಅಲ್ಲ. "
                    "ಉಳಿದ ಮೂರು ವಸ್ತುಗಳ ಮೇಲೆ ಕೆಲಸ ಮಾಡುವ ಬಲಗಳು."
                ),
                "difficulty": 1,
            },
            {
                "question_en": "Friction always acts…",
                "question_kn": "ಘರ್ಷಣೆ ಯಾವಾಗಲೂ ಯಾವ ದಿಕ್ಕಿನಲ್ಲಿ ಕೆಲಸ ಮಾಡುತ್ತದೆ?",
                "options_en": [
                    "in the direction of sliding",
                    "opposite to the direction of sliding",
                    "upwards only",
                    "only on rough ground",
                ],
                "options_kn": [
                    "ಜಾರುವಿಕೆಯ ದಿಕ್ಕಿನಲ್ಲಿ",
                    "ಜಾರುವಿಕೆಯ ವಿರುದ್ಧ ದಿಕ್ಕಿನಲ್ಲಿ",
                    "ಮೇಲ್ಮುಖವಾಗಿ ಮಾತ್ರ",
                    "ಒರಟು ನೆಲದಲ್ಲಿ ಮಾತ್ರ",
                ],
                "correct_index": 1,
                "explanation_en": (
                    "Friction opposes relative motion between surfaces, so it points against the "
                    "sliding direction and slows the object."
                ),
                "explanation_kn": (
                    "ಘರ್ಷಣೆ ಮೇಲ್ಮೈಗಳ ನಡುವಿನ ಚಲನೆಯನ್ನು ವಿರೋಧಿಸುತ್ತದೆ; "
                    "ಆದ್ದರಿಂದ ಅದು ಜಾರುವಿಕೆಯ ವಿರುದ್ಧ ದಿಕ್ಕಿನಲ್ಲಿದ್ದು ವಸ್ತುವನ್ನು "
                    "ನಿಧಾನಗೊಳಿಸುತ್ತದೆ."
                ),
                "difficulty": 1,
            },
            {
                "question_en": "Why is oil added to a machine's moving parts?",
                "question_kn": "ಯಂತ್ರದ ಚಲಿಸುವ ಭಾಗಗಳಿಗೆ ಎಣ್ಣೆ ಏಕೆ ಹಾಕುತ್ತಾರೆ?",
                "options_en": [
                    "To increase friction",
                    "To reduce friction and wear",
                    "To make the parts heavier",
                    "To increase gravity",
                ],
                "options_kn": [
                    "ಘರ್ಷಣೆ ಹೆಚ್ಚಿಸಲು",
                    "ಘರ್ಷಣೆ ಮತ್ತು ಸವೆತ ಕಡಿಮೆ ಮಾಡಲು",
                    "ಭಾಗಗಳನ್ನು ಭಾರವಾಗಿಸಲು",
                    "ಗುರುತ್ವ ಹೆಚ್ಚಿಸಲು",
                ],
                "correct_index": 1,
                "explanation_en": (
                    "Oil forms a thin film between surfaces so they slide over each other instead "
                    "of catching. Less friction means less wear and less wasted heat."
                ),
                "explanation_kn": (
                    "ಎಣ್ಣೆ ಮೇಲ್ಮೈಗಳ ನಡುವೆ ತೆಳು ಪೊರೆ ಉಂಟುಮಾಡಿ ಅವು ಸಿಕ್ಕಿಕೊಳ್ಳದೆ "
                    "ಜಾರುವಂತೆ ಮಾಡುತ್ತದೆ. ಘರ್ಷಣೆ ಕಡಿಮೆಯಾದರೆ ಸವೆತ ಮತ್ತು "
                    "ವ್ಯರ್ಥ ಉಷ್ಣ ಕಡಿಮೆಯಾಗುತ್ತದೆ."
                ),
                "difficulty": 2,
            },
            {
                "question_en": "A mango falls from a tree because of…",
                "question_kn": "ಮರದಿಂದ ಮಾವು ಯಾವ ಬಲದಿಂದ ಕೆಳಗೆ ಬೀಳುತ್ತದೆ?",
                "options_en": ["Gravity", "Friction", "Magnetism", "Air pressure only"],
                "options_kn": ["ಗುರುತ್ವ", "ಘರ್ಷಣೆ", "ಕಾಂತತ್ವ", "ಗಾಳಿಯ ಒತ್ತಡ ಮಾತ್ರ"],
                "correct_index": 0,
                "explanation_en": (
                    "Gravity pulls the mango towards the Earth's centre. Air resistance only "
                    "slows the fall slightly."
                ),
                "explanation_kn": (
                    "ಗುರುತ್ವ ಮಾವನ್ನು ಭೂಮಿಯ ಕೇಂದ್ರದ ಕಡೆಗೆ ಎಳೆಯುತ್ತದೆ. "
                    "ಗಾಳಿಯ ಪ್ರತಿರೋಧ ಬೀಳುವಿಕೆಯನ್ನು ಸ್ವಲ್ಪ ಮಾತ್ರ "
                    "ನಿಧಾನಗೊಳಿಸುತ್ತದೆ."
                ),
                "difficulty": 1,
            },
            {
                "question_en": "An astronaut's mass on the Moon compared with Earth is…",
                "question_kn": "ಭೂಮಿಗೆ ಹೋಲಿಸಿದರೆ ಚಂದ್ರನ ಮೇಲೆ ಗಗನಯಾತ್ರಿಯ ರಾಶಿ ಎಷ್ಟು?",
                "options_en": [
                    "one-sixth as much",
                    "six times more",
                    "exactly the same",
                    "zero",
                ],
                "options_kn": [
                    "ಆರರಲ್ಲಿ ಒಂದು ಭಾಗ",
                    "ಆರು ಪಟ್ಟು ಹೆಚ್ಚು",
                    "ಸಂಪೂರ್ಣ ಸಮಾನ",
                    "ಶೂನ್ಯ",
                ],
                "correct_index": 2,
                "explanation_en": (
                    "Mass is the amount of matter and does not depend on where you are. Only "
                    "weight, the pull of gravity, becomes about one-sixth."
                ),
                "explanation_kn": (
                    "ರಾಶಿ ಎಂದರೆ ಪದಾರ್ಥದ ಪ್ರಮಾಣ; ಅದು ನೀವು ಎಲ್ಲಿದ್ದೀರಿ ಎಂಬುದನ್ನು "
                    "ಅವಲಂಬಿಸಿಲ್ಲ. ಗುರುತ್ವದ ಎಳೆಯುವಿಕೆಯಾದ ತೂಕ ಮಾತ್ರ ಸುಮಾರು "
                    "ಆರರಲ್ಲಿ ಒಂದು ಭಾಗವಾಗುತ್ತದೆ."
                ),
                "difficulty": 3,
            },
        ],
    },
    {
        "number": 5,
        "category": "physics",
        "is_enrichment": False,
        "title_en": "Light: Mirrors and Lenses",
        "title_kn": "ಬೆಳಕು: ಕನ್ನಡಿಗಳು ಮತ್ತು ಮಸೂರಗಳು",
        "summary_en": (
            "Trace how light bounces off mirrors and bends through lenses, and learn why a "
            "concave mirror can start a fire while a convex lens corrects your eyesight."
        ),
        "summary_kn": (
            "ಬೆಳಕು ಕನ್ನಡಿಗಳಿಂದ ಹೇಗೆ ಪ್ರತಿಫಲನಗೊಳ್ಳುತ್ತದೆ ಮತ್ತು ಮಸೂರಗಳ ಮೂಲಕ "
            "ಹೇಗೆ ಬಾಗುತ್ತದೆ ಎಂಬುದನ್ನು ಅನುಸರಿಸಿ; ನಿಮ್ನ ಕನ್ನಡಿ ಬೆಂಕಿ "
            "ಹಚ್ಚಬಲ್ಲದು ಏಕೆ, ಪೀನ ಮಸೂರ ಕಣ್ಣಿನ ದೃಷ್ಟಿ ಸರಿಪಡಿಸುತ್ತದೆ ಏಕೆ "
            "ಎಂಬುದನ್ನು ತಿಳಿಯಿರಿ."
        ),
        "estimated_minutes": 45,
        "visualizations": ["light"],
        "topics": [
            {
                "title_en": "Reflection of light",
                "title_kn": "ಬೆಳಕಿನ ಪ್ರತಿಫಲನ",
                "objectives_en": [
                    "Identify the incident ray, reflected ray and normal.",
                    "State the law of reflection.",
                ],
                "objectives_kn": [
                    "ಪತನ ಕಿರಣ, ಪ್ರತಿಫಲಿತ ಕಿರಣ ಮತ್ತು ಲಂಬವನ್ನು ಗುರುತಿಸುವುದು.",
                    "ಪ್ರತಿಫಲನದ ನಿಯಮವನ್ನು ಹೇಳುವುದು.",
                ],
                "body_en": [
                    "Light travels in straight lines. When it strikes a polished surface, most of "
                    "it bounces back: this is reflection. Draw a line perpendicular to the mirror "
                    "at the point where light lands and you have the normal. The incoming ray is "
                    "the incident ray, the returning one is the reflected ray, and the angle each "
                    "makes with the normal is the angle of incidence and the angle of reflection.",
                    "The law of reflection says these two angles are always equal. That is why a "
                    "plane mirror image looks as far behind the mirror as you stand in front of "
                    "it, and why it is reversed left to right. A rough surface reflects light in "
                    "many directions at once, so you see brightness but no image; a smooth surface "
                    "reflects in one direction, so you see a clear image.",
                ],
                "body_kn": [
                    "ಬೆಳಕು ನೇರ ರೇಖೆಯಲ್ಲಿ ಸಾಗುತ್ತದೆ. ಅದು ನಯವಾದ ಮೇಲ್ಮೈಗೆ ಬಿದ್ದಾಗ "
                    "ಹೆಚ್ಚಿನ ಭಾಗ ಹಿಂತಿರುಗುತ್ತದೆ: ಇದೇ ಪ್ರತಿಫಲನ. ಬೆಳಕು ಬಿದ್ದ "
                    "ಸ್ಥಳದಲ್ಲಿ ಕನ್ನಡಿಗೆ ಲಂಬವಾಗಿ ರೇಖೆ ಎಳೆದರೆ ಅದು ಲಂಬ. ಒಳಬರುವ "
                    "ಕಿರಣ ಪತನ ಕಿರಣ, ಹಿಂತಿರುಗುವ ಕಿರಣ ಪ್ರತಿಫಲಿತ ಕಿರಣ; ಪ್ರತಿಯೊಂದೂ "
                    "ಲಂಬದೊಂದಿಗೆ ಮಾಡುವ ಕೋನವೇ ಪತನ ಕೋನ ಮತ್ತು ಪ್ರತಿಫಲನ ಕೋನ.",
                    "ಪ್ರತಿಫಲನದ ನಿಯಮದ ಪ್ರಕಾರ ಈ ಎರಡು ಕೋನಗಳು ಯಾವಾಗಲೂ ಸಮ. ಆದ್ದರಿಂದ "
                    "ಸಮತಲ ಕನ್ನಡಿಯಲ್ಲಿ ನೀವು ಕನ್ನಡಿಯ ಮುಂದೆ ನಿಂತಷ್ಟೇ ದೂರದಲ್ಲಿ "
                    "ಪ್ರತಿಬಿಂಬ ಕಾಣುತ್ತದೆ ಮತ್ತು ಅದು ಎಡ-ಬಲ "
                    "ಬದಲಾಗಿರುತ್ತದೆ. ಒರಟು ಮೇಲ್ಮೈ ಬೆಳಕನ್ನು ಅನೇಕ ದಿಕ್ಕುಗಳಲ್ಲಿ "
                    "ಪ್ರತಿಫಲಿಸುತ್ತದೆ; ಆದ್ದರಿಂದ ಬೆಳಕು ಕಾಣುತ್ತದೆ, ಪ್ರತಿಬಿಂಬ "
                    "ಕಾಣುವುದಿಲ್ಲ. ನಯ ಮೇಲ್ಮೈ ಒಂದೇ ದಿಕ್ಕಿನಲ್ಲಿ ಪ್ರತಿಫಲಿಸುತ್ತದೆ; "
                    "ಆದ್ದರಿಂದ ಸ್ಪಷ್ಟ ಪ್ರತಿಬಿಂಬ ಕಾಣುತ್ತದೆ.",
                ],
                "key_terms": [
                    {
                        "kn": "ಪ್ರತಿಫಲನ",
                        "en": "Reflection",
                        "meaning_kn": "ಬೆಳಕು ಮೇಲ್ಮೈಗೆ ಬಿದ್ದು ಹಿಂತಿರುಗುವ ಕ್ರಿಯೆ.",
                        "meaning_en": "Light bouncing back from a surface.",
                    },
                    {
                        "kn": "ಲಂಬ",
                        "en": "Normal",
                        "meaning_kn": "ಕನ್ನಡಿಗೆ ಲಂಬವಾಗಿ ಎಳೆದ ಕಾಲ್ಪನಿಕ ರೇಖೆ.",
                        "meaning_en": "An imaginary line drawn perpendicular to the mirror.",
                    },
                ],
                "example_en": (
                    "A periscope in a submarine uses two plane mirrors at 45° to bend light twice, "
                    "letting a sailor see above the water."
                ),
                "example_kn": (
                    "ಜಲಾಂತರ್ಗಾಮಿಯ ಪೆರಿಸ್ಕೋಪ್ 45° ಕೋನದಲ್ಲಿರುವ ಎರಡು ಸಮತಲ "
                    "ಕನ್ನಡಿಗಳನ್ನು ಬಳಸಿ ಬೆಳಕನ್ನು ಎರಡು ಬಾರಿ ಬಾಗಿಸುತ್ತದೆ; "
                    "ಆದ್ದರಿಂದ ನಾವಿಕನಿಗೆ ನೀರಿನ ಮೇಲಿನ ದೃಶ್ಯ ಕಾಣುತ್ತದೆ."
                ),
            },
            {
                "title_en": "Concave and convex mirrors",
                "title_kn": "ನಿಮ್ನ ಮತ್ತು ಪೀನ ಕನ್ನಡಿಗಳು",
                "objectives_en": [
                    "Describe the shape of concave and convex mirrors.",
                    "Match each mirror to a real use.",
                ],
                "objectives_kn": [
                    "ನಿಮ್ನ ಮತ್ತು ಪೀನ ಕನ್ನಡಿಗಳ ಆಕಾರವನ್ನು ವಿವರಿಸುವುದು.",
                    "ಪ್ರತಿ ಕನ್ನಡಿಯನ್ನು ನಿಜವಾದ ಉಪಯೋಗಕ್ಕೆ ಹೊಂದಿಸುವುದು.",
                ],
                "body_en": [
                    "A curved mirror is a part of a sphere. If the reflecting surface curves "
                    "inwards like the inside of a spoon, it is concave; if it bulges outwards like "
                    "the back of the spoon, it is convex. A concave mirror brings parallel rays "
                    "together at a focus, so it can concentrate sunlight enough to burn paper.",
                    "A convex mirror spreads rays outwards, so it shows a wide field of view in a "
                    "small mirror. That is why it is used at blind corners, in shop security "
                    "corners and as a vehicle's side mirror, where the warning 'objects are closer "
                    "than they appear' reminds us that the image is small. Concave mirrors are used "
                    "in torches, headlights, dentist's mirrors and solar cookers. A concave mirror "
                    "can also form a real image on a screen; a convex mirror never does.",
                ],
                "body_kn": [
                    "ಬಾಗಿದ ಕನ್ನಡಿ ಗೋಳದ ಒಂದು ಭಾಗ. ಪ್ರತಿಫಲಿಸುವ ಮೇಲ್ಮೈ ಚಮಚದ "
                    "ಒಳಭಾಗದಂತೆ ಒಳಮುಖವಾಗಿ ಬಾಗಿದ್ದರೆ ಅದು ನಿಮ್ನ ಕನ್ನಡಿ; ಚಮಚದ "
                    "ಹಿಂಭಾಗದಂತೆ ಹೊರಮುಖವಾಗಿ ಉಬ್ಬಿದ್ದರೆ ಅದು ಪೀನ ಕನ್ನಡಿ. "
                    "ನಿಮ್ನ ಕನ್ನಡಿ ಸಮಾನಾಂತರ ಕಿರಣಗಳನ್ನು ಒಂದೇ ಬಿಂದುವಿನಲ್ಲಿ "
                    "(ಕೇಂದ್ರಬಿಂದು) ಸೇರಿಸುತ್ತದೆ; ಆದ್ದರಿಂದ ಸೂರ್ಯನ ಬೆಳಕನ್ನು "
                    "ಸಾಂದ್ರೀಕರಿಸಿ ಕಾಗದ ಸುಡಬಲ್ಲದು.",
                    "ಪೀನ ಕನ್ನಡಿ ಕಿರಣಗಳನ್ನು ಹೊರಕ್ಕೆ ಹರಡುತ್ತದೆ; ಆದ್ದರಿಂದ ಸಣ್ಣ "
                    "ಕನ್ನಡಿಯಲ್ಲೂ ಅಗಲವಾದ ದೃಶ್ಯ ಕಾಣುತ್ತದೆ. ಆದ್ದರಿಂದಲೇ ಅದನ್ನು "
                    "ಕುರುಡು ತಿರುವು, ಅಂಗಡಿಯ ಭದ್ರತಾ ಮೂಲೆ ಮತ್ತು ವಾಹನದ ಪಾರ್ಶ್ವ "
                    "ಕನ್ನಡಿಯಲ್ಲಿ ಬಳಸುತ್ತಾರೆ; 'ವಸ್ತುಗಳು ಕಾಣುವುದಕ್ಕಿಂತ ಹತ್ತಿರವಿವೆ' "
                    "ಎಂಬ ಎಚ್ಚರಿಕೆ ಪ್ರತಿಬಿಂಬ ಚಿಕ್ಕದಾಗಿರುವುದನ್ನು ನೆನಪಿಸುತ್ತದೆ. "
                    "ನಿಮ್ನ ಕನ್ನಡಿಗಳನ್ನು ಟಾರ್ಚ್, ಹೆಡ್‌ಲೈಟ್, ದಂತವೈದ್ಯರ ಕನ್ನಡಿ "
                    "ಮತ್ತು ಸೌರ ಕುಕ್ಕರ್‌ಗಳಲ್ಲಿ ಬಳಸುತ್ತಾರೆ. ನಿಮ್ನ ಕನ್ನಡಿ "
                    "ಪರದೆಯ ಮೇಲೆ ನಿಜವಾದ ಪ್ರತಿಬಿಂಬವನ್ನೂ ಉಂಟುಮಾಡಬಲ್ಲದು; "
                    "ಪೀನ ಕನ್ನಡಿ ಎಂದೂ ಸಾಧ್ಯವಿಲ್ಲ.",
                ],
                "key_terms": [
                    {
                        "kn": "ನಿಮ್ನ ಕನ್ನಡಿ",
                        "en": "Concave mirror",
                        "meaning_kn": "ಒಳಮುಖವಾಗಿ ಬಾಗಿದ ಪ್ರತಿಫಲಿಸುವ ಮೇಲ್ಮೈ.",
                        "meaning_en": "A mirror whose reflecting surface curves inwards.",
                    },
                    {
                        "kn": "ಪೀನ ಕನ್ನಡಿ",
                        "en": "Convex mirror",
                        "meaning_kn": "ಹೊರಮುಖವಾಗಿ ಉಬ್ಬಿದ ಪ್ರತಿಫಲಿಸುವ ಮೇಲ್ಮೈ.",
                        "meaning_en": "A mirror whose reflecting surface bulges outwards.",
                    },
                ],
                "example_en": (
                    "A solar cooker lined with a concave mirror focuses sunlight on the vessel and "
                    "cooks rice without any fuel."
                ),
                "example_kn": (
                    "ನಿಮ್ನ ಕನ್ನಡಿಯಿಂದ ಒಳಪಸಿಯಾದ ಸೌರ ಕುಕ್ಕರ್ ಸೂರ್ಯನ ಬೆಳಕನ್ನು "
                    "ಪಾತ್ರೆಯ ಮೇಲೆ ಕೇಂದ್ರೀಕರಿಸಿ ಯಾವುದೇ ಇಂಧನವಿಲ್ಲದೆ ಅನ್ನ "
                    "ಬೇಯಿಸುತ್ತದೆ."
                ),
            },
            {
                "title_en": "Lenses",
                "title_kn": "ಮಸೂರಗಳು",
                "objectives_en": [
                    "Compare convex and concave lenses.",
                    "Explain how a convex lens forms an image.",
                ],
                "objectives_kn": [
                    "ಪೀನ ಮತ್ತು ನಿಮ್ನ ಮಸೂರಗಳನ್ನು ಹೋಲಿಸುವುದು.",
                    "ಪೀನ ಮಸೂರ ಪ್ರತಿಬಿಂಬವನ್ನು ಹೇಗೆ ಉಂಟುಮಾಡುತ್ತದೆ ಎಂಬುದನ್ನು ವಿವರಿಸುವುದು.",
                ],
                "body_en": [
                    "A lens is a piece of transparent material with curved surfaces that bends "
                    "light by refraction. A convex lens is thicker in the middle and converges "
                    "parallel rays to a focus; a concave lens is thinner in the middle and spreads "
                    "them apart. This bending happens because light changes speed when it passes "
                    "from air into glass and back again.",
                    "A magnifying glass is a convex lens. Hold it close to a page and you see an "
                    "enlarged, upright image; hold it far from a window and it forms a small, "
                    "inverted real image on a wall. A camera, a projector and the eye all use "
                    "convex lenses. Concave lenses are used in spectacles for short-sighted people, "
                    "because they spread the rays so the image falls correctly on the retina. "
                    "Spectacle prescriptions are always given in dioptres, a unit of lens power.",
                ],
                "body_kn": [
                    "ಮಸೂರ ಎಂದರೆ ಬಾಗಿದ ಮೇಲ್ಮೈ ಇರುವ ಪಾರದರ್ಶಕ ಪದಾರ್ಥ; ಅದು "
                    "ವಕ್ರೀಭವನದಿಂದ ಬೆಳಕನ್ನು ಬಾಗಿಸುತ್ತದೆ. ಪೀನ ಮಸೂರ ಮಧ್ಯದಲ್ಲಿ "
                    "ದಪ್ಪವಾಗಿದ್ದು ಸಮಾನಾಂತರ ಕಿರಣಗಳನ್ನು ಕೇಂದ್ರಬಿಂದುವಿನಲ್ಲಿ "
                    "ಸೇರಿಸುತ್ತದೆ; ನಿಮ್ನ ಮಸೂರ ಮಧ್ಯದಲ್ಲಿ ತೆಳುವಾಗಿದ್ದು ಅವನ್ನು "
                    "ಹರಡುತ್ತದೆ. ಬೆಳಕು ಗಾಳಿಯಿಂದ ಗಾಜಿಗೆ, ಮತ್ತೆ ಗಾಳಿಗೆ ಹಾದುಹೋಗುವಾಗ "
                    "ವೇಗ ಬದಲಾಗುವುದರಿಂದ ಈ ಬಾಗುವಿಕೆ ಉಂಟಾಗುತ್ತದೆ.",
                    "ಭೂತಗನ್ನಡಿ ಒಂದು ಪೀನ ಮಸೂರ. ಅದನ್ನು ಪುಟಕ್ಕೆ ಹತ್ತಿರ ಹಿಡಿದರೆ "
                    "ದೊಡ್ಡದಾದ, ನೇರ ಪ್ರತಿಬಿಂಬ ಕಾಣುತ್ತದೆ; ಕಿಟಕಿಗೆ ದೂರ ಹಿಡಿದರೆ "
                    "ಗೋಡೆಯ ಮೇಲೆ ಚಿಕ್ಕದಾದ, ತಲೆಕೆಳಗಾದ ನಿಜ ಪ್ರತಿಬಿಂಬ "
                    "ಉಂಟಾಗುತ್ತದೆ. ಕ್ಯಾಮೆರಾ, ಪ್ರೊಜೆಕ್ಟರ್ ಮತ್ತು ಕಣ್ಣು ಎಲ್ಲವೂ "
                    "ಪೀನ ಮಸೂರ ಬಳಸುತ್ತವೆ. ಸಮೀಪ ದೃಷ್ಟಿ ದೋಷವಿರುವವರ ಕನ್ನಡಕದಲ್ಲಿ "
                    "ನಿಮ್ನ ಮಸೂರ ಬಳಸುತ್ತಾರೆ; ಏಕೆಂದರೆ ಅದು ಕಿರಣಗಳನ್ನು ಹರಡಿ "
                    "ಪ್ರತಿಬಿಂಬ ರೆಟಿನಾದ ಮೇಲೆ ಸರಿಯಾಗಿ ಬೀಳುವಂತೆ ಮಾಡುತ್ತದೆ. "
                    "ಕನ್ನಡಕದ ಶಕ್ತಿಯನ್ನು ಯಾವಾಗಲೂ ಡಯೋಪ್ಟರ್ ಏಕಮಾನದಲ್ಲಿ "
                    "ಹೇಳುತ್ತಾರೆ.",
                ],
                "key_terms": [
                    {
                        "kn": "ವಕ್ರೀಭವನ",
                        "en": "Refraction",
                        "meaning_kn": "ಬೆಳಕು ಒಂದು ಮಾಧ್ಯಮದಿಂದ ಇನ್ನೊಂದಕ್ಕೆ ಹೋಗುವಾಗ ಬಾಗುವುದು.",
                        "meaning_en": "The bending of light as it passes between media.",
                    },
                    {
                        "kn": "ಪೀನ ಮಸೂರ",
                        "en": "Convex lens",
                        "meaning_kn": "ಮಧ್ಯದಲ್ಲಿ ದಪ್ಪವಾಗಿದ್ದು ಕಿರಣಗಳನ್ನು ಸೇರಿಸುವ ಮಸೂರ.",
                        "meaning_en": "A lens that is thick in the middle and converges rays.",
                    },
                ],
                "example_en": (
                    "Sunlight through a convex lens can burn a dry leaf: the lens converges all "
                    "that light into one small, hot spot."
                ),
                "example_kn": (
                    "ಪೀನ ಮಸೂರದ ಮೂಲಕ ಬಿದ್ದ ಸೂರ್ಯನ ಬೆಳಕು ಒಣ ಎಲೆಯನ್ನು ಸುಡಬಲ್ಲದು: "
                    "ಮಸೂರ ಆ ಬೆಳಕನ್ನೆಲ್ಲಾ ಒಂದು ಸಣ್ಣ, ಬಿಸಿ ಬಿಂದುವಿನಲ್ಲಿ "
                    "ಸೇರಿಸುತ್ತದೆ."
                ),
            },
        ],
        "notes_en": [
            "Light travels in straight lines and reflects from polished surfaces.",
            "Angle of incidence equals angle of reflection; both are measured from the normal.",
            "A plane mirror forms an upright image as far behind as the object is in front.",
            "Concave mirrors converge light; used in torches, solar cookers, dentist's mirrors.",
            "Convex mirrors diverge light and give a wide view; used at corners and in vehicles.",
            "A convex lens converges rays and can magnify; a concave lens diverges them.",
            "Refraction is the bending of light when it changes medium and speed.",
        ],
        "notes_kn": [
            "ಬೆಳಕು ನೇರ ರೇಖೆಯಲ್ಲಿ ಸಾಗಿ ನಯ ಮೇಲ್ಮೈಯಿಂದ ಪ್ರತಿಫಲನಗೊಳ್ಳುತ್ತದೆ.",
            "ಪತನ ಕೋನ ಮತ್ತು ಪ್ರತಿಫಲನ ಕೋನ ಸಮಾನ; ಎರಡನ್ನೂ ಲಂಬದಿಂದ ಅಳೆಯುತ್ತಾರೆ.",
            "ಸಮತಲ ಕನ್ನಡಿ ನೇರ ಪ್ರತಿಬಿಂಬವನ್ನು ವಸ್ತುವಿನಷ್ಟೇ ದೂರದಲ್ಲಿ ಉಂಟುಮಾಡುತ್ತದೆ.",
            "ನಿಮ್ನ ಕನ್ನಡಿ ಬೆಳಕನ್ನು ಸೇರಿಸುತ್ತದೆ; ಟಾರ್ಚ್, ಸೌರ ಕುಕ್ಕರ್, ದಂತವೈದ್ಯರ ಕನ್ನಡಿಯಲ್ಲಿ ಬಳಕೆ.",
            "ಪೀನ ಕನ್ನಡಿ ಬೆಳಕನ್ನು ಹರಡಿ ಅಗಲ ದೃಶ್ಯ ನೀಡುತ್ತದೆ; ತಿರುವು ಮತ್ತು ವಾಹನಗಳಲ್ಲಿ ಬಳಕೆ.",
            "ಪೀನ ಮಸೂರ ಕಿರಣಗಳನ್ನು ಸೇರಿಸಿ ದೊಡ್ಡದಾಗಿಸಬಲ್ಲದು; ನಿಮ್ನ ಮಸೂರ ಅವನ್ನು ಹರಡುತ್ತದೆ.",
            "ವಕ್ರೀಭವನ ಎಂದರೆ ಬೆಳಕು ಮಾಧ್ಯಮ ಮತ್ತು ವೇಗ ಬದಲಾದಾಗ ಬಾಗುವುದು.",
        ],
        "videos": [
            {
                "title": "ಬೆಳಕು: ಕನ್ನಡಿ ಮತ್ತು ಮಸೂರ — ಕನ್ನಡ",
                "language": "kn",
                "topic": "Light and reflection",
                "search_query": "ಬೆಳಕು ಪ್ರತಿಫಲನ ಕನ್ನಡಿ ಮಸೂರ ಕನ್ನಡ 8ನೇ ತರಗತಿ",
            },
            {
                "title": "Light, mirrors and lenses for Class 8",
                "language": "en",
                "topic": "Light and reflection",
                "search_query": "light reflection mirrors lenses class 8 science lesson",
            },
        ],
        "quiz": [
            {
                "question_en": "The angle of incidence is measured between the incident ray and the…",
                "question_kn": "ಪತನ ಕೋನವನ್ನು ಪತನ ಕಿರಣ ಮತ್ತು ಯಾವುದರ ನಡುವೆ ಅಳೆಯುತ್ತಾರೆ?",
                "options_en": ["mirror surface", "normal", "reflected ray", "focus"],
                "options_kn": ["ಕನ್ನಡಿಯ ಮೇಲ್ಮೈ", "ಲಂಬ", "ಪ್ರತಿಫಲಿತ ಕಿರಣ", "ಕೇಂದ್ರಬಿಂದು"],
                "correct_index": 1,
                "explanation_en": (
                    "Both angles are measured from the normal, the line perpendicular to the "
                    "mirror at the point of incidence. That is what makes the law symmetric."
                ),
                "explanation_kn": (
                    "ಎರಡೂ ಕೋನಗಳನ್ನು ಲಂಬದಿಂದ ಅಳೆಯುತ್ತಾರೆ; ಲಂಬ ಎಂದರೆ ಪತನ "
                    "ಬಿಂದುವಿನಲ್ಲಿ ಕನ್ನಡಿಗೆ ಲಂಬವಾಗಿ ಎಳೆದ ರೇಖೆ. ಆದ್ದರಿಂದಲೇ "
                    "ನಿಯಮ ಸಮರೂಪವಾಗಿದೆ."
                ),
                "difficulty": 2,
            },
            {
                "question_en": "Which mirror is used as a vehicle's side mirror to give a wide view?",
                "question_kn": "ಅಗಲವಾದ ದೃಶ್ಯ ನೀಡಲು ವಾಹನದ ಪಾರ್ಶ್ವ ಕನ್ನಡಿಯಾಗಿ ಯಾವ ಕನ್ನಡಿ ಬಳಸುತ್ತಾರೆ?",
                "options_en": ["Plane mirror", "Concave mirror", "Convex mirror", "No mirror"],
                "options_kn": ["ಸಮತಲ ಕನ್ನಡಿ", "ನಿಮ್ನ ಕನ್ನಡಿ", "ಪೀನ ಕನ್ನಡಿ", "ಕನ್ನಡಿ ಬೇಡ"],
                "correct_index": 2,
                "explanation_en": (
                    "A convex mirror spreads rays and shows a wider field of view in a small "
                    "mirror, though the image is smaller than the object."
                ),
                "explanation_kn": (
                    "ಪೀನ ಕನ್ನಡಿ ಕಿರಣಗಳನ್ನು ಹರಡಿ ಸಣ್ಣ ಕನ್ನಡಿಯಲ್ಲೂ ಅಗಲವಾದ "
                    "ದೃಶ್ಯ ತೋರಿಸುತ್ತದೆ; ಆದರೆ ಪ್ರತಿಬಿಂಬ ವಸ್ತುವಿಗಿಂತ ಚಿಕ್ಕದು."
                ),
                "difficulty": 1,
            },
            {
                "question_en": "A magnifying glass is which type of lens?",
                "question_kn": "ಭೂತಗನ್ನಡಿ ಯಾವ ಬಗೆಯ ಮಸೂರ?",
                "options_en": ["Concave lens", "Convex lens", "Plane lens", "Cylindrical mirror"],
                "options_kn": ["ನಿಮ್ನ ಮಸೂರ", "ಪೀನ ಮಸೂರ", "ಸಮತಲ ಮಸೂರ", "ಸ್ತಂಭಾಕಾರ ಕನ್ನಡಿ"],
                "correct_index": 1,
                "explanation_en": (
                    "A convex lens converges light. Held near an object it forms an enlarged, "
                    "upright image, which is what magnifying means."
                ),
                "explanation_kn": (
                    "ಪೀನ ಮಸೂರ ಬೆಳಕನ್ನು ಸೇರಿಸುತ್ತದೆ. ವಸ್ತುವಿನ ಹತ್ತಿರ ಹಿಡಿದಾಗ "
                    "ದೊಡ್ಡದಾದ, ನೇರ ಪ್ರತಿಬಿಂಬ ಉಂಟಾಗುತ್ತದೆ; ಇದೇ "
                    "ವರ್ಧನೆಯ ಅರ್ಥ."
                ),
                "difficulty": 1,
            },
            {
                "question_en": "Why does a concave mirror burn paper in sunlight?",
                "question_kn": "ನಿಮ್ನ ಕನ್ನಡಿ ಬಿಸಿಲಿನಲ್ಲಿ ಕಾಗದವನ್ನು ಏಕೆ ಸುಡುತ್ತದೆ?",
                "options_en": [
                    "It creates its own heat",
                    "It converges sunlight to a small bright spot",
                    "It blocks sunlight completely",
                    "It spreads light over a large area",
                ],
                "options_kn": [
                    "ಅದು ತನ್ನದೇ ಉಷ್ಣ ಉತ್ಪಾದಿಸುತ್ತದೆ",
                    "ಸೂರ್ಯನ ಬೆಳಕನ್ನು ಸಣ್ಣ ಪ್ರಕಾಶಮಾನ ಬಿಂದುವಿನಲ್ಲಿ ಸೇರಿಸುತ್ತದೆ",
                    "ಬಿಸಿಲನ್ನು ಸಂಪೂರ್ಣ ತಡೆಯುತ್ತದೆ",
                    "ಬೆಳಕನ್ನು ದೊಡ್ಡ ಪ್ರದೇಶದಲ್ಲಿ ಹರಡುತ್ತದೆ",
                ],
                "correct_index": 1,
                "explanation_en": (
                    "Concentrating the same light into a small area raises the temperature sharply "
                    "at that spot, enough to char paper."
                ),
                "explanation_kn": (
                    "ಅದೇ ಬೆಳಕನ್ನು ಸಣ್ಣ ಪ್ರದೇಶದಲ್ಲಿ ಸೇರಿಸಿದಾಗ ಆ ಬಿಂದುವಿನ "
                    "ತಾಪಮಾನ ತೀವ್ರವಾಗಿ ಹೆಚ್ಚಿ ಕಾಗದ ಕರಕಲಾಗುತ್ತದೆ."
                ),
                "difficulty": 2,
            },
            {
                "question_en": "Which statement about reflection is always true?",
                "question_kn": "ಪ್ರತಿಫಲನದ ಬಗ್ಗೆ ಯಾವ ಹೇಳಿಕೆ ಯಾವಾಗಲೂ ನಿಜ?",
                "options_en": [
                    "The reflected ray is longer than the incident ray",
                    "The angle of reflection equals the angle of incidence",
                    "The image is always larger than the object",
                    "Light bends when it reflects",
                ],
                "options_kn": [
                    "ಪ್ರತಿಫಲಿತ ಕಿರಣ ಪತನ ಕಿರಣಕ್ಕಿಂತ ಉದ್ದ",
                    "ಪ್ರತಿಫಲನ ಕೋನ ಪತನ ಕೋನಕ್ಕೆ ಸಮ",
                    "ಪ್ರತಿಬಿಂಬ ಯಾವಾಗಲೂ ವಸ್ತುವಿಗಿಂತ ದೊಡ್ಡದು",
                    "ಪ್ರತಿಫಲನದಲ್ಲಿ ಬೆಳಕು ಬಾಗುತ್ತದೆ",
                ],
                "correct_index": 1,
                "explanation_en": (
                    "The equality of the two angles holds for every polished surface, flat or "
                    "curved. Size of the image is not fixed by this law."
                ),
                "explanation_kn": (
                    "ಎರಡು ಕೋನಗಳ ಸಮಾನತೆ ಸಮತಲ ಅಥವಾ ಬಾಗಿದ ಎಲ್ಲಾ ನಯ "
                    "ಮೇಲ್ಮೈಗಳಿಗೂ ಅನ್ವಯಿಸುತ್ತದೆ. ಪ್ರತಿಬಿಂಬದ ಗಾತ್ರವನ್ನು "
                    "ಈ ನಿಯಮ ನಿರ್ಧರಿಸುವುದಿಲ್ಲ."
                ),
                "difficulty": 3,
            },
        ],
    },
)
