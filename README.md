# 🎓 Linux Essentials Quiz Engine

**🇬🇧 English Version** | **[🇩🇪 Deutsche Version](README_DE.md)**

---

An interactive quiz system for Linux Essentials 010-160 exam preparation with 276 official exam questions, multiple quiz modes, and realistic exam simulation.

---

## ✨ Features

### 🎯 Two Versions Available

**🐍 Python Terminal Version** (`quiz_engine.py`)
- Terminal-based quiz with live countdown timer
- Single-keypress input (no Enter needed!)
- Built-in question editor (open fragen.json from menu)
- Weighted exam mode (LPI-compliant topic distribution)
- Real-time timer display during questions
- Cross-platform (Windows/Linux/macOS)

**🌐 Web Browser Version** (`index.html`)
- Beautiful web interface with modern design
- No installation needed - just open in browser
- Weighted exam mode with 800-point scoring system
- Instant explanations for wrong answers
- Mobile-friendly responsive layout

### 📚 Core Features (Both Versions)

- ✅ **276 Official Questions** - Complete Linux Essentials 010-160 coverage
- ✅ **3 Quiz Modes:**
  - **Learning Mode:** All 276 questions, no time limit
  - **Exam Mode:** 40 questions, 60 minutes, weighted by LPI topics
  - **Custom Mode:** Choose any number of questions
- ✅ **Smart Randomization:**
  - Questions in random order
  - Answers shuffled (A-D) to prevent memorization
- ✅ **Statistics & Evaluation:**
  - Percentage score
  - Pass/Fail indicator (≥60% / ≥500 points)
  - Time tracking in Exam mode
- ✅ **Add Your Own Questions** - Easy JSON format (see guide below)

---

## 🎮 Quick Start

### 🌐 Web Version (Easiest)

1. Download or clone the repository
2. Open `index.html` in your browser
3. Start learning!

**No installation needed!** ✅

### 🐍 Python Terminal Version

```bash
# Clone repository
git clone https://github.com/MCCMDave/linux-essentials-quiz.git
cd linux-essentials-quiz

# Run Python quiz
python quiz_engine.py
```

**Requirements:** Python 3.10+ (no external dependencies!)

---

## 📊 Question Database

**fragen.json** contains 276 exam questions from all official topics.

### Category Distribution

| Category | Count |
|----------|-------|
| 1.1 Linux Evolution | 28 |
| 4.3 Where Data is Stored | 27 |
| 4.4 Computer on Network | 26 |
| 3.2 Searching and Extracting | 24 |
| 2.1 Command Line Basics | 21 |
| 3.3 Shell Scripting | 19 |
| 4.2 Computer Hardware | 18 |
| 1.2 Open Source Applications | 16 |
| 4.1 Choosing an OS | 14 |
| *...and 10 more* | 83 |

---

## 🎯 Creating Your Own Question Catalog

Want to create a quiz for a different exam or topic? Easy!

### JSON Structure

```json
{
  "metadata": {
    "version": "1.0",
    "datum": "November 2025",
    "total_fragen": 276,
    "kategorien": {
      "1.1 Linux Evolution": 28,
      "1.2 Open Source Applications": 16
    },
    "beschreibung": "Your Quiz Topic"
  },
  "fragen": [
    {
      "frage": "Your question here?",
      "optionen": [
        "Answer option A",
        "Answer option B",
        "Answer option C",
        "Answer option D"
      ],
      "richtige_antwort": 1,
      "kategorie": "Category Name"
    }
  ]
}
```

### Field Explanation

- **frage**: Your question text
- **optionen**: Array with exactly 4 answer options
- **richtige_antwort**: Index of correct answer (0=A, 1=B, 2=C, 3=D)
- **kategorie**: Topic/category name

### Steps to Create Your Own Quiz

1. **Copy Template**
   ```bash
   cp fragen.json my-quiz.json
   ```

2. **Edit JSON** - Add your questions following the structure above
   - Each question needs exactly 4 options
   - Index starts at 0 (A=0, B=1, C=2, D=3)
   - UTF-8 encoding for special characters

3. **Update Metadata**
   ```json
   "metadata": {
     "total_fragen": 50,  # Update to your count
     "beschreibung": "My Custom Quiz"
   }
   ```

4. **Modify Python File** (optional)
   - Open `quiz_engine.py`
   - Line ~15: Change `'fragen.json'` to `'my-quiz.json'`

5. **Run Your Quiz**
   ```bash
   python quiz_engine.py
   ```

### Tips for Creating Questions

✅ **Do:**
- Keep questions clear and concise
- Use exactly 4 answer options
- Include one obviously wrong answer
- Group by categories for better organization
- Test your JSON syntax (use online validators)

❌ **Don't:**
- Use more or fewer than 4 options
- Forget to update `richtige_antwort` index
- Mix up indices (remember: starts at 0!)
- Use special quotes ("" instead of "" "")

---

## 🎓 Menu-Based Question Management

### Adding Questions via Menu (Future Feature)

Currently in development! Soon you'll be able to:
- Add new questions interactively
- Edit existing questions
- Delete questions
- Export to new JSON file

**Want this feature now?** Let me know via [GitHub Issues](https://github.com/MCCMDave/linux-essentials-quiz/issues)!

---

## 🎮 Usage

### Main Menu
```
==============================================================================================
==                                   CHOOSE QUIZ MODE                                       ==
==============================================================================================
==                                                                                          ==
==                          [1] Learning Mode - All Questions (276)                        ==
==                          [2] Exam Mode - 40 Questions, 60 Min                           ==
==                          [3] Custom - Choose Number                                     ==
==                          [0] Exit                                                       ==
==                                                                                          ==
==============================================================================================
```

### Mode Details

#### 🎓 Learning Mode
- All 276 questions
- No time limit
- Immediate feedback
- Perfect for comprehensive study

#### ⏱️ Exam Mode
- 40 questions with **LPI-weighted topic distribution**:
  - Topic 1: 7 questions (17.5%)
  - Topic 2: 9 questions (22.5%)
  - Topic 3: 9 questions (22.5%)
  - Topic 4: 8 questions (20%)
  - Topic 5: 7 questions (17.5%)
- 60 minute timer (Python: live countdown!)
- Time warning at <5 minutes
- Pass/Fail display (≥60% or ≥500 points)
- Realistic exam simulation

#### 🎛️ Custom Mode
- Choose 1-276 questions
- No time limit
- Flexible practice

#### 📝 Question Editor (Python only)
- Built-in menu option to edit questions
- Opens `fragen.json` in your default editor
- Access to `FRAGEN-HINZUFUEGEN.md` guide
- Quick and easy question management

---

## 🎓 Linux Essentials Certification

Based on **Linux Essentials 010-160 v1.6** exam format.

### Exam Details
- **Duration:** 60 minutes
- **Questions:** 40 multiple-choice
- **Format:** 4 answer options (A-D)
- **Passing Score:** ~60% (24/40 correct)

### Topic Coverage

| Topic | Weight | Questions |
|-------|--------|-----------|
| 1. Linux Community & Open Source | 17.5% | 7 |
| 2. Finding Your Way | 22.5% | 9 |
| 3. The Power of the Command Line | 25% | 10 |
| 4. The Linux Operating System | 27.5% | 11 |
| 5. Security & File Permissions | 7.5% | 3 |

---

## 📁 Project Structure

```
linux-essentials-quiz/
├── index.html                  # 🌐 Web version (browser-based)
├── quiz_engine.py              # 🐍 Python terminal version (main)
├── fragen.json                 # Question database (276 questions)
├── FRAGEN-HINZUFUEGEN.md       # Guide for adding questions
├── README.md                   # English documentation
├── README_DE.md                # German documentation
└── LICENSE                     # Apache 2.0 License
```

---

## 🛠️ Tech Stack

### 🌐 Web Version
**Technologies:**
- HTML5 - Structure
- CSS3 - Modern styling with gradients
- JavaScript (ES6+) - Quiz logic and interactivity
- No frameworks needed!

**Features:**
- Responsive design (mobile-friendly)
- 800-point scoring system
- Instant answer explanations
- Progress bar and stats

### 🐍 Python Version
**Python 3.10+ with Standard Library:**
- `json` - Question database loading
- `random` - Shuffling and randomization
- `time` - Timer and countdown functionality
- `threading` - Live timer display
- `os` / `sys` - Cross-platform file opening

**No external dependencies!** ✅

---

## 📄 License

**Apache License 2.0** - Free to use, modify, and distribute for personal and commercial use.

See [LICENSE](LICENSE) file for details.

---

## 👨‍💻 Author

**David Vaupel**
Python Developer | Linux Essentials Certified (85%+)

- 📧 Contact via [GitHub Issues](https://github.com/MCCMDave/linux-essentials-quiz/issues)
- 💼 [LinkedIn](https://www.linkedin.com/in/david-vaupel)
- 🐙 GitHub: [@MCCMDave](https://github.com/MCCMDave)

---

## 🔗 Related Projects

- [Python Learning](https://github.com/MCCMDave/python-learning) - Complete Python learning journey
- [Homelab Automation](https://github.com/MCCMDave/homelab-automation) - Homelab monitoring tools
- [Windows Automation](https://github.com/MCCMDave/windows-automation) - Windows automation scripts

---

## 📝 Changelog

### v2.2 (November 2025) - Simplified Structure
- ✅ **Single-Keypress Input:** No Enter needed for answers (A/B/C/D)
- ✅ **Cleaner Structure:** Removed legacy v1, renamed v2 to main version
- ✅ **Visual Feedback:** Answer display with "==" indicator
- ✅ **README Cleanup:** Updated documentation for new structure

### v2.1 (November 2025) - Python Enhancements
- ✅ **Live Timer:** Real-time countdown display during questions
- ✅ **Weighted Exam:** LPI-compliant topic distribution in exam mode
- ✅ **Question Editor:** Built-in menu to edit fragen.json
- ✅ **UI Improvements:** Better visual separation with divider lines

### v2.0 (November 2025) - Web & Python
- ✅ Web version (index.html) with modern UI
- ✅ Python version with JSON database (276 questions)
- ✅ 3 quiz modes (Learning/Exam/Custom)
- ✅ Timer system for exam mode

---

## 💡 Contributing

Want to contribute questions or improve the quiz?

1. Fork the repository
2. Add your questions to `fragen.json`
3. Test thoroughly
4. Submit a Pull Request

**Question contributions welcome!** Especially for:
- Additional Linux certifications (LPIC-1, RHCSA)
- Other IT certifications
- Programming language quizzes

---

**Status:** ✅ Production Ready
**Last Update:** November 2025

---

**[⬆ Back to top](#-linux-essentials-quiz-engine)**
