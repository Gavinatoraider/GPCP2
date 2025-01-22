# Jackson Hauley - Personal Library Program

import random

# Initializing Variables

library_name = "My Library"
library = set({})
id = 0


# Essential Functions
def int_input(text): # Only takes in integers
    while True:
        try: output = int(input(text))
        except ValueError:
            print("Invalid Input! (only integers accepted)")
            input("Press enter to try again")
            continue
        return output
def str_input(text): # Only takes in string
    while True:
        try: output = str(input(text))
        except ValueError:
            print("String Input! (only strings accepted)")
            input("Press enter to try again")
            continue
        return output
def float_input(text): # Only takes in floats
    while True:
        try: output = float(input(text))
        except ValueError:
            print("Invalid Input! (only floats accepted)")
            input("Press enter to try again")
            continue
        return output
def cs(): # Clear Screen
    print("\033c",end="")

# Main Funcitons
def main():
    global library_name,library,id
    while True:
        cs()
        choice = int_input("Personal Library\n\n1. Search Library\n2. Add Item\n3. Remove Item\n4. Erase Library\n5. Generate Random Books\n6. Rename Library\n7. View Library\n8. Exit Library\n\nWhat do you want to do? (1-8): ")
        if choice == 1: # Search Item choice
            search_library() # Search Item function
        elif choice == 2: # Adding item choice
            add_item() # Add item function
        elif choice == 3: # Remove item choice
            remove_item() # Remove item function
        elif choice == 4: # Deleting the entire library choice
            sure = input("Are you sure you want to reset your library? (type yes, anything else will cancel): ")
            if sure.lower() == "yes":
                print("Library reset!")
                library = set({})
                input("Press enter to continue")
            else:
                print("Glad you decided not too!")
                input("press enter to continue")

        elif choice == 5: # Randomly generate books
            cs()
            amount = int_input("How many random books do you want to generate?: ")
            print()
            for x in range(amount):
                book = random.choice(["ability", "able", "about", "above", "accept", "according", "account", "across", "act", "action", "activity", "actually", "add", "address", "administration", "admit", "adult", "affect", "after", "again", "against", "age", "agency", "agent", "ago", "agree", "agreement", "ahead", "air", "all", "allow", "almost", "alone", "along", "already", "also", "although", "always", "American", "among", "amount", "analysis", "and", "animal", "another", "answer", "any", "anyone", "anything", "appear", "apply", "approach", "area", "argue", "arm", "around", "arrive", "art", "article", "artist", "as", "ask", "assume", "at", "attack", "attention", "attorney", "audience", "author", "authority", "available", "avoid", "away", "baby", "back", "bad", "bag", "ball", "bank", "bar", "base", "be", "beat", "beautiful", "because", "become", "bed", "before", "begin", "behavior", "behind", "believe", "benefit", "best", "better", "between", "beyond", "big", "bill", "billion", "bit", "black", "blood", "blue", "board", "body", "book", "born", "both", "box", "boy", "break", "bring", "brother", "budget", "build", "building", "business", "but", "buy", "by", "call", "camera", "campaign", "can", "cancer", "candidate", "capital", "car", "card", "care", "career", "carry", "case", "catch", "cause", "cell", "center", "central", "century", "certain", "certainly", "chair", "challenge", "chance", "change", "character", "charge", "check", "child", "choice", "choose", "church", "citizen", "city", "civil", "claim", "class", "clear", "clearly", "close", "coach", "cold", "collection", "college", "color", "come", "commercial", "common", "community", "company", "compare", "computer", "concern", "condition", "conference", "Congress", "consider", "consumer", "contain", "continue", "control", "cost", "could", "country", "couple", "course", "court", "cover", "create", "crime", "cultural", "culture", "cup", "current", "customer", "cut", "dark", "data", "daughter", "day", "dead", "deal", "death", "debate", "decade", "decide", "decision", "deep", "defense", "degree", "Democrat", "democratic", "describe", "design", "despite", "detail", "determine", "develop", "development", "die", "difference", "different", "difficult", "dinner", "direction", "director", "discover", "discuss", "discussion", "disease", "do", "doctor", "dog", "door", "down", "draw", "dream", "drive", "drop", "drug", "during", "each", "early", "east", "easy", "eat", "economic", "economy", "edge", "education", "effect", "effort", "eight", "either", "election", "else", "employee", "end", "energy", "enjoy", "enough", "enter", "entire", "environment", "environmental", "especially", "establish", "even", "evening", "event", "ever", "every", "everybody", "everyone", "everything", "evidence", "exactly", "example", "executive", "exist", "expect", "experience", "expert", "explain", "eye", "face", "fact", "factor", "fail", "fall", "family", "far", "fast", "father", "fear", "federal", "feel", "feeling", "few", "field", "fight", "figure", "fill", "film", "final", "finally", "financial", "find", "fine", "finger", "finish", "fire", "firm", "first", "fish", "five", "floor", "fly", "focus", "follow", "food", "foot", "for", "force", "foreign", "forget", "form", "former", "forward", "four", "free", "friend", "from", "front", "full", "fund", "future", "game", "garden", "gas", "general", "generation", "get", "girl", "give", "glass", "go", "goal", "good", "government", "great", "green", "ground", "group", "grow", "growth", "guess", "gun", "guy", "hair", "half", "hand", "hang", "happen", "happy", "hard", "have", "he", "head", "health", "hear", "heart", "heat", "heavy", "help", "her", "here", "herself", "high", "him", "himself", "his", "history", "hit", "hold", "home", "hope", "hospital", "hot", "hotel", "hour", "house", "how", "however", "huge", "human", "hundred", "husband", "I", "idea", "identify", "if", "image", "imagine", "impact", "important", "improve", "in", "include", "including", "increase", "indeed", "indicate", "individual", "industry", "information", "inside", "instead", "institution", "interest", "interesting", "international", "interview", "into", "investment", "involve", "issue", "it", "item", "its", "itself", "job", "join", "just", "keep", "key", "kid", "kill", "kind", "kitchen", "know", "knowledge", "land", "language", "large", "last", "late", "later", "laugh", "law", "lawyer", "lay", "lead", "leader", "learn", "least", "leave", "left", "leg", "legal", "less", "let", "letter", "level", "lie", "life", "light", "like", "likely", "line", "list", "listen", "little", "live", "local", "long", "look", "lose", "loss", "lot", "love", "low", "machine", "magazine", "main", "maintain", "major", "majority", "make", "man", "manage", "management", "manager", "many", "market", "marriage", "material", "matter", "may", "maybe", "me", "mean", "measure", "media", "medical", "meet", "meeting", "member", "memory", "mention", "message", "method", "middle", "might", "military", "million", "mind", "minute", "miss", "mission", "model", "modern", "moment", "money", "month", "more", "morning", "most", "mother", "mouth", "move", "movement", "movie", "Mr", "Mrs", "much", "music", "must", "my", "myself", "name", "nation", "national", "natural", "nature", "near", "nearly", "necessary", "need", "network", "never", "new", "news", "newspaper", "next", "nice", "night", "no", "none", "nor", "north", "not", "note", "nothing", "notice", "now","number", "occur", "of", "off", "offer", "office", "officer", "official", "often", "oh", "oil", "ok", "old", "on", "once", "one", "only", "onto", "open", "operation", "opportunity", "option", "or", "order", "organization", "other", "others", "our", "out", "outside", "over", "own", "owner", "page", "pain", "painting", "paper", "parent", "part", "participant", "particular", "particularly", "partner", "party", "pass", "past", "patient", "pattern", "pay", "peace", "people", "per", "perform", "performance", "perhaps", "period", "person", "personal", "phone", "physical", "pick", "picture", "piece", "place", "plan", "plant", "play", "player", "PM", "point", "police", "policy", "political", "politics", "poor", "popular", "population", "position", "positive", "possible", "power", "practice", "prepare", "present", "president", "pressure", "pretty", "prevent", "price", "private", "probably", "problem", "process", "produce", "product", "production", "professional", "professor", "program", "project", "property", "protect", "prove", "provide", "public", "pull", "purpose", "push", "put", "quality", "question", "quickly", "quite", "race", "radio", "raise", "range", "rate", "rather", "reach", "read", "ready", "real", "reality", "realize", "really", "reason", "receive", "recent", "recently", "recognize", "record", "red", "reduce", "reflect", "region", "relate", "relationship", "religious", "remain", "remember", "remove", "report", "represent", "Republican", "require", "research", "resource", "respond", "response", "responsibility", "rest", "result", "return", "reveal", "rich", "right", "rise", "risk", "road", "rock", "role", "room", "rule", "run", "safe", "same", "save", "say", "scene", "school", "science", "scientist", "score", "sea", "season", "seat", "second", "section", "security", "see", "seek", "seem", "sell", "send", "senior", "sense", "series", "serious", "serve", "service", "set", "seven", "several", "shake", "share", "she", "shoot", "short", "shot", "should", "shoulder", "show", "side", "sign", "significant", "similar", "simple", "simply", "since", "sing", "single", "sister", "sit", "site", "situation", "six", "size", "skill", "skin", "small", "smile", "so", "social", "society", "soldier", "some", "somebody", "someone", "something", "sometimes", "son", "song", "soon", "sort", "sound", "source", "south", "southern", "space", "speak", "special", "specific", "speech", "spend", "sport", "spring", "staff", "stage", "stand", "standard", "star", "start", "state", "statement", "station", "stay", "step", "still", "stock", "stop", "store", "story", "strategy", "street", "strong", "structure", "student", "study", "stuff", "style", "subject", "success", "successful", "such", "suddenly", "suffer", "suggest", "summer", "support", "sure", "surface", "system", "table", "take", "talk", "task", "tax", "teach", "teacher", "team", "technology", "television", "tell", "ten", "tend", "term", "test", "than", "thank", "that", "the", "their", "them", "themselves", "then", "theory", "there", "these", "they", "thing", "think", "third", "this", "those", "though", "thought", "thousand", "threat", "three", "through", "throughout", "throw", "thus", "time", "to", "today", "together", "tonight", "too", "top", "total", "tough", "toward", "town", "trade", "traditional", "training", "travel", "treat", "treatment", "tree", "trial", "trip", "trouble", "true", "truth", "try", "turn", "TV", "two", "type", "under", "understand", "unit", "until", "up", "upon", "us", "use", "usually", "value", "various", "very", "victim", "view", "violence", "visit", "voice", "vote", "wait", "walk", "wall", "want", "war", "watch", "water", "way", "we", "weapon", "wear", "week", "weight", "well", "west", "western", "what", "whatever", "when", "where", "whether", "which", "while", "white", "who", "whole", "whom", "whose", "why", "wide", "wife", "will", "win", "wind", "window", "wish", "with", "within", "without", "woman", "wonder", "word", "work", "worker", "world", "worry", "would", "write", "writer", "wrong", "yard", "yeah", "year", "yes", "yet", "you", "young", "your", "yourself","balls"])
                book2 = random.choice(["ability", "able", "about", "above", "accept", "according", "account", "across", "act", "action", "activity", "actually", "add", "address", "administration", "admit", "adult", "affect", "after", "again", "against", "age", "agency", "agent", "ago", "agree", "agreement", "ahead", "air", "all", "allow", "almost", "alone", "along", "already", "also", "although", "always", "American", "among", "amount", "analysis", "and", "animal", "another", "answer", "any", "anyone", "anything", "appear", "apply", "approach", "area", "argue", "arm", "around", "arrive", "art", "article", "artist", "as", "ask", "assume", "at", "attack", "attention", "attorney", "audience", "author", "authority", "available", "avoid", "away", "baby", "back", "bad", "bag", "ball", "bank", "bar", "base", "be", "beat", "beautiful", "because", "become", "bed", "before", "begin", "behavior", "behind", "believe", "benefit", "best", "better", "between", "beyond", "big", "bill", "billion", "bit", "black", "blood", "blue", "board", "body", "book", "born", "both", "box", "boy", "break", "bring", "brother", "budget", "build", "building", "business", "but", "buy", "by", "call", "camera", "campaign", "can", "cancer", "candidate", "capital", "car", "card", "care", "career", "carry", "case", "catch", "cause", "cell", "center", "central", "century", "certain", "certainly", "chair", "challenge", "chance", "change", "character", "charge", "check", "child", "choice", "choose", "church", "citizen", "city", "civil", "claim", "class", "clear", "clearly", "close", "coach", "cold", "collection", "college", "color", "come", "commercial", "common", "community", "company", "compare", "computer", "concern", "condition", "conference", "Congress", "consider", "consumer", "contain", "continue", "control", "cost", "could", "country", "couple", "course", "court", "cover", "create", "crime", "cultural", "culture", "cup", "current", "customer", "cut", "dark", "data", "daughter", "day", "dead", "deal", "death", "debate", "decade", "decide", "decision", "deep", "defense", "degree", "Democrat", "democratic", "describe", "design", "despite", "detail", "determine", "develop", "development", "die", "difference", "different", "difficult", "dinner", "direction", "director", "discover", "discuss", "discussion", "disease", "do", "doctor", "dog", "door", "down", "draw", "dream", "drive", "drop", "drug", "during", "each", "early", "east", "easy", "eat", "economic", "economy", "edge", "education", "effect", "effort", "eight", "either", "election", "else", "employee", "end", "energy", "enjoy", "enough", "enter", "entire", "environment", "environmental", "especially", "establish", "even", "evening", "event", "ever", "every", "everybody", "everyone", "everything", "evidence", "exactly", "example", "executive", "exist", "expect", "experience", "expert", "explain", "eye", "face", "fact", "factor", "fail", "fall", "family", "far", "fast", "father", "fear", "federal", "feel", "feeling", "few", "field", "fight", "figure", "fill", "film", "final", "finally", "financial", "find", "fine", "finger", "finish", "fire", "firm", "first", "fish", "five", "floor", "fly", "focus", "follow", "food", "foot", "for", "force", "foreign", "forget", "form", "former", "forward", "four", "free", "friend", "from", "front", "full", "fund", "future", "game", "garden", "gas", "general", "generation", "get", "girl", "give", "glass", "go", "goal", "good", "government", "great", "green", "ground", "group", "grow", "growth", "guess", "gun", "guy", "hair", "half", "hand", "hang", "happen", "happy", "hard", "have", "he", "head", "health", "hear", "heart", "heat", "heavy", "help", "her", "here", "herself", "high", "him", "himself", "his", "history", "hit", "hold", "home", "hope", "hospital", "hot", "hotel", "hour", "house", "how", "however", "huge", "human", "hundred", "husband", "I", "idea", "identify", "if", "image", "imagine", "impact", "important", "improve", "in", "include", "including", "increase", "indeed", "indicate", "individual", "industry", "information", "inside", "instead", "institution", "interest", "interesting", "international", "interview", "into", "investment", "involve", "issue", "it", "item", "its", "itself", "job", "join", "just", "keep", "key", "kid", "kill", "kind", "kitchen", "know", "knowledge", "land", "language", "large", "last", "late", "later", "laugh", "law", "lawyer", "lay", "lead", "leader", "learn", "least", "leave", "left", "leg", "legal", "less", "let", "letter", "level", "lie", "life", "light", "like", "likely", "line", "list", "listen", "little", "live", "local", "long", "look", "lose", "loss", "lot", "love", "low", "machine", "magazine", "main", "maintain", "major", "majority", "make", "man", "manage", "management", "manager", "many", "market", "marriage", "material", "matter", "may", "maybe", "me", "mean", "measure", "media", "medical", "meet", "meeting", "member", "memory", "mention", "message", "method", "middle", "might", "military", "million", "mind", "minute", "miss", "mission", "model", "modern", "moment", "money", "month", "more", "morning", "most", "mother", "mouth", "move", "movement", "movie", "Mr", "Mrs", "much", "music", "must", "my", "myself", "name", "nation", "national", "natural", "nature", "near", "nearly", "necessary", "need", "network", "never", "new", "news", "newspaper", "next", "nice", "night", "no", "none", "nor", "north", "not", "note", "nothing", "notice", "now", "number", "occur", "of", "off", "offer", "office", "officer", "official", "often", "oh", "oil", "ok", "old", "on", "once", "one", "only", "onto", "open", "operation", "opportunity", "option", "or", "order", "organization", "other", "others", "our", "out", "outside", "over", "own", "owner", "page", "pain", "painting", "paper", "parent", "part", "participant", "particular", "particularly", "partner", "party", "pass", "past", "patient", "pattern", "pay", "peace", "people", "per", "perform", "performance", "perhaps", "period", "person", "personal", "phone", "physical", "pick", "picture", "piece", "place", "plan", "plant", "play", "player", "PM", "point", "police", "policy", "political", "politics", "poor", "popular", "population", "position", "positive", "possible", "power", "practice", "prepare", "present", "president", "pressure", "pretty", "prevent", "price", "private", "probably", "problem", "process", "produce", "product", "production", "professional", "professor", "program", "project", "property", "protect", "prove", "provide", "public", "pull", "purpose", "push", "put", "quality", "question", "quickly", "quite", "race", "radio", "raise", "range", "rate", "rather", "reach", "read", "ready", "real", "reality", "realize", "really", "reason", "receive", "recent", "recently", "recognize", "record", "red", "reduce", "reflect", "region", "relate", "relationship", "religious", "remain", "remember", "remove", "report", "represent", "Republican", "require", "research", "resource", "respond", "response", "responsibility", "rest", "result", "return", "reveal", "rich", "right", "rise", "risk", "road", "rock", "role", "room", "rule", "run", "safe", "same", "save", "say", "scene", "school", "science", "scientist", "score", "sea", "season", "seat", "second", "section", "security", "see", "seek", "seem", "sell", "send", "senior", "sense", "series", "serious", "serve", "service", "set", "seven", "several", "shake", "share", "she", "shoot", "short", "shot", "should", "shoulder", "show", "side", "sign", "significant", "similar", "simple", "simply", "since", "sing", "single", "sister", "sit", "site", "situation", "six", "size", "skill", "skin", "small", "smile", "so", "social", "society", "soldier", "some", "somebody", "someone", "something", "sometimes", "son", "song", "soon", "sort", "sound", "source", "south", "southern", "space", "speak", "special", "specific", "speech", "spend", "sport", "spring", "staff", "stage", "stand", "standard", "star", "start", "state", "statement", "station", "stay", "step", "still", "stock", "stop", "store", "story", "strategy", "street", "strong", "structure", "student", "study", "stuff", "style", "subject", "success", "successful", "such", "suddenly", "suffer", "suggest", "summer", "support", "sure", "surface", "system", "table", "take", "talk", "task", "tax", "teach", "teacher", "team", "technology", "television", "tell", "ten", "tend", "term", "test", "than", "thank", "that", "the", "their", "them", "themselves", "then", "theory", "there", "these", "they", "thing", "think", "third", "this", "those", "though", "thought", "thousand", "threat", "three", "through", "throughout", "throw", "thus", "time", "to", "today", "together", "tonight", "too", "top", "total", "tough", "toward", "town", "trade", "traditional", "training", "travel", "treat", "treatment", "tree", "trial", "trip", "trouble", "true", "truth", "try", "turn", "TV", "two", "type", "under", "understand", "unit", "until", "up", "upon", "us", "use", "usually", "value", "various", "very", "victim", "view", "violence", "visit", "voice", "vote", "wait", "walk", "wall", "want", "war", "watch", "water", "way", "we", "weapon", "wear", "week", "weight", "well", "west", "western", "what", "whatever", "when", "where", "whether", "which", "while", "white", "who", "whole", "whom", "whose", "why", "wide", "wife", "will", "win", "wind", "window", "wish", "with", "within", "without", "woman", "wonder", "word", "work", "worker", "world", "worry", "would", "write", "writer", "wrong", "yard", "yeah", "year", "yes", "yet", "you", "young", "your", "yourself","balls","",""])
                book = f"{book.title()} {book2.title()}"
                author = random.choice([ "Johnson","Dwane","Cage","Gage","Haggard","Hauley","Pierce","Liam", "Noah", "Oliver", "Elijah", "James", "William", "Benjamin", "Lucas", "Henry", "Alexander", "Mason", "Michael", "Ethan", "Daniel", "Jacob", "Jackson", "Sebastian", "Jack", "Aiden", "Owen", "Samuel", "Matthew","Gavin", "Joseph", "Levi", "Mateo", "David", "John", "Wyatt", "Carter", "Julian", "Luke", "Hudson", "Grayson", "Isaac", "Gabriel", "Anthony", "Dylan", "Leo", "Lincoln", "Jaxon", "Asher", "Christopher", "Maverick", "Elias", "Joshua", "Andrew", "Theodore", "Caleb", "Ryan", "Adrian", "Thomas", "Charles", "Ezekiel", "Nathan", "Miles", "Dominic", "Xavier", "Isaiah", "Zachary", "Thomas", "Christian", "Joshua", "Hunter", "Cameron", "Carter", "Jace", "Jesse", "Everett", "Santiago", "Cole", "Nolan", "Jeremiah", "Easton", "Angel", "Brayden", "Maxwell", "Josiah", "Ryan", "Jason", "Jaxson", "Robert", "Jameson", "Asher", "Levi", "Lincoln", "Benjamin", "Sebastian", "Oliver", "Henry", "Joseph", "William", "Jackson", "Carter", "David", "Daniel", "Matthew", "Eli", "Jackson", "Lucas", "Levi", "Samuel", "Alexander", "Luke", "Wyatt", "Carter", "Julian", "Wyatt", "Owen", "William", "Elliott", "Ryan", "Elijah", "Harrison", "Milo", "Connor", "Adam", "Cooper", "David", "Victor", "Ezra", "Hank", "Derek", "Ethan", "Micheal", "Charles", "Oliver", "Arthur", "Martin", "Landon", "Theo", "Gabriel", "Mason", "Evan", "Patrick", "Noah", "James", "Wyatt", "Ryan", "Blake", "Harrison", "Lucas", "Caden", "Liam", "Toby", "Levi", "Joseph", "Vincent", "Mason", "Nicholas", "Troy", "Julian", "Hunter", "Alex", "Miles", "Elias", "Nolan", "Nathan", "Joseph", "Luca", "Kai", "Caleb", "Evan", "Ryan", "Jacob", "Carter", "Maverick", "Benjamin", "Max", "James", "Levi", "Isaac", "Benjamin", "Aaron", "Asher", "Easton", "Hunter", "Zayden", "Blake", "Elijah", "James", "Owen", "Mathew", "Adrian", "Jaxon", "Nathan", "Joshua", "David", "Matthew", "Tyler", "Jacob", "Sebastian", "Caleb", "Bryce", "Isaiah", "Hunter", "Liam", "Luke", "Jackson", "Caleb", "Hudson", "Adam", "John", "Carter", "Cameron", "Max", "Ryan", "Jaxon", "Lucas", "Bryson", "Noah", "Eli", "Wyatt", "Julian", "Cole", "Isaac", "Ezra", "Aaron", "Victor", "Angel", "Elijah", "Dominic", "Ezra", "Sebastian", "Carter", "Jameson", "Luke", "Santiago", "Matthew", "Levi", "Xander", "Mason", "David", "Oliver", "Eli", "Henry", "Abel", "Antonio", "Roman", "Diego", "Alexander", "Elliott", "Matthew", "Evan", "Nolan", "Aiden", "Isaiah", "James", "Robert", "Lucas", "Cameron", "Isaac", "Lucas", "Blake", "Ryan", "Hudson", "Thomas", "Samuel", "Nicholas", "Carter", "Isaac", "Jaxson", "Jackson", "Levi", "Andrew", "Jason", "Caleb", "Luke", "Benjamin", "Maverick", "Caleb", "David", "Jack", "Gabriel", "Oliver", "Liam", "Ryan", "Zachary", "Mason", "Milo", "Luke", "Theo", "Leo", "Maxwell", "Robert", "Nolan", "Charles", "Gabriel", "Lucas", "Miles", "Jaxon", "Blake", "Asher", "Miles", "Noah", "Owen", "Adam", "Wyatt", "Isaac", "Zachary", "John", "Ryan", "Sebastian", "Jacob", "Matthew", "Levi", "Adrian", "Jason", "Nolan", "Mason", "Lucas", "Jackson", "Julian", "Elijah", "Milo", "Matthew", "Tyler", "Eli", "Benjamin", "Asher", "Robert", "Oliver", "Ezekiel", "Maverick", "Andrew", "Elijah", "James", "Zachary", "Owen", "Sebastian", "Caleb", "David", "Miles", "Carter", "Eli", "Sebastian", "Isaac", "Wyatt", "Jack", "Andrew", "Gabriel", "Matthew", "Grayson", "David", "Lucas", "Ezekiel", "Adam", "Elijah", "Maverick", "Mason", "Thomas", "Elijah", "Asher", "Sebastian", "Xavier", "Lucas", "Carter", "Hudson", "Zane", "Cameron", "Benjamin", "Levi", "William", "Lucas", "Eli", "Maxwell", "Hudson", "Landon", "Levi", "Roman", "Santiago", "Milo", "Maverick", "Carter", "Liam", "Caden", "Isaiah", "Samuel", "Ryan", "Jack", "Joshua", "Jameson", "Jacob", "Michael", "Luca", "Levi", "Asher", "Nicholas", "Caleb", "Eli", "Miles", "Wyatt", "Ezra", "Ryan", "Sebastian", "Mason", "Nolan", "Elijah", "Isaac", "Jackson", "Carter", "Gabriel", "Lucas", "Leo", "Isaiah", "Julian", "Jack", "Levi", "Mason", "Oliver", "Hudson", "Evan", "Hudson", "Noah", "Sebastian", "David", "Milo", "Aiden", "Zachary", "Blake", "Ezekiel", "Maverick", "Samuel", "Julian", "Santiago", "Xander", "Liam", "Jacob", "Adrian", "Caleb", "Jacob", "David", "Lucas", "Maverick", "Miles", "Eli", "Ethan", "Daniel", "Hudson", "Noah", "Zachary", "Owen", "Nolan", "Elijah", "Isaac", "Hudson", "Ezra", "Hunter", "Wyatt", "Eli", "Aiden", "Sebastian", "Caleb", "Jameson", "Eli", "Maverick", "Asher", "Jaxon", "Noah", "Ezekiel", "Lucas", "Roman", "Asher", "Carter", "Ezra", "Benjamin", "Hudson", "Zachary", "Sebastian", "Maverick", "Isaac", "James", "Noah", "Luke", "Jack", "Levi", "Aiden", "Jacob", "Mason", "Carter", "Wyatt", "Lucas", "Maverick", "Hudson", "Levi", "Sebastian", "David", "Santiago", "Jameson", "Lucas", "Leo", "Caden", "Hudson", "Julian", "Miles", "Zachary", "Cameron", "Isaiah", "Hudson", "Maverick", "Levi", "Mason", "Sebastian", "Blake", "Wyatt", "Ezra", "Zachary","Balls"])
                author2 = random.choice(["Johnson","Dwane","Cage","Haggard","Pierce","Liam", "Noah", "Oliver", "Elijah", "James", "William", "Benjamin", "Lucas", "Henry", "Alexander", "Mason", "Michael", "Ethan", "Daniel", "Jacob", "Jackson", "Sebastian", "Jack", "Aiden", "Owen", "Samuel", "Matthew", "Joseph", "Levi", "Mateo", "David", "John", "Wyatt", "Carter", "Julian", "Luke", "Hudson", "Grayson", "Isaac", "Gabriel", "Anthony", "Dylan", "Leo", "Lincoln", "Jaxon", "Asher", "Christopher", "Maverick", "Elias", "Joshua", "Andrew", "Theodore", "Caleb", "Ryan", "Adrian", "Thomas", "Charles", "Ezekiel", "Nathan", "Miles", "Dominic", "Xavier", "Isaiah", "Zachary", "Thomas", "Christian", "Joshua", "Hunter", "Cameron", "Carter", "Jace", "Jesse", "Everett", "Santiago", "Cole", "Nolan", "Jeremiah", "Easton", "Angel", "Brayden", "Maxwell", "Josiah", "Ryan", "Jason", "Jaxson", "Robert", "Jameson", "Asher", "Levi", "Lincoln", "Benjamin", "Sebastian", "Oliver", "Henry", "Joseph", "William", "Jackson", "Carter", "David", "Daniel", "Matthew", "Eli", "Jackson", "Lucas", "Levi", "Samuel", "Alexander", "Luke", "Wyatt", "Carter", "Julian", "Wyatt", "Owen", "William", "Elliott", "Ryan", "Elijah", "Harrison", "Milo", "Connor", "Adam", "Cooper", "David", "Victor", "Ezra", "Hank", "Derek", "Ethan", "Micheal", "Charles", "Oliver", "Arthur", "Martin", "Landon", "Theo", "Gabriel", "Mason", "Evan", "Patrick", "Noah", "James", "Wyatt", "Ryan", "Blake", "Harrison", "Lucas", "Caden", "Liam", "Toby", "Levi", "Joseph", "Vincent", "Mason", "Nicholas", "Troy", "Julian", "Hunter", "Alex", "Miles", "Elias", "Nolan", "Nathan", "Joseph", "Luca", "Kai", "Caleb", "Evan", "Ryan", "Jacob", "Carter", "Maverick", "Benjamin", "Max", "James", "Levi", "Isaac", "Benjamin", "Aaron", "Asher", "Easton", "Hunter", "Zayden", "Blake", "Elijah", "James", "Owen", "Mathew", "Adrian", "Jaxon", "Nathan", "Joshua", "David", "Matthew", "Tyler", "Jacob", "Sebastian", "Caleb", "Bryce", "Isaiah", "Hunter", "Liam", "Luke", "Jackson", "Caleb", "Hudson", "Adam", "John", "Carter", "Cameron", "Max", "Ryan", "Jaxon", "Lucas", "Bryson", "Noah", "Eli", "Wyatt", "Julian", "Cole", "Isaac", "Ezra", "Aaron", "Victor", "Angel", "Elijah", "Dominic", "Ezra", "Sebastian", "Carter", "Jameson", "Luke", "Santiago", "Matthew", "Levi", "Xander", "Mason", "David", "Oliver", "Eli", "Henry", "Abel", "Antonio", "Roman", "Diego", "Alexander", "Elliott", "Matthew", "Evan", "Nolan", "Aiden", "Isaiah", "James", "Robert", "Lucas", "Cameron", "Isaac", "Lucas", "Blake", "Ryan", "Hudson", "Thomas", "Samuel", "Nicholas", "Carter", "Isaac", "Jaxson", "Jackson", "Levi", "Andrew", "Jason", "Caleb", "Luke", "Benjamin", "Maverick", "Caleb", "David", "Jack", "Gabriel", "Oliver", "Liam", "Ryan", "Zachary", "Mason", "Milo", "Luke", "Theo", "Leo", "Maxwell", "Robert", "Nolan", "Charles", "Gabriel", "Lucas", "Miles", "Jaxon", "Blake", "Asher", "Miles", "Noah", "Owen", "Adam", "Wyatt", "Isaac", "Zachary", "John", "Ryan", "Sebastian", "Jacob", "Matthew", "Levi", "Adrian", "Jason", "Nolan", "Mason", "Lucas", "Jackson", "Julian", "Elijah", "Milo", "Matthew", "Tyler", "Eli", "Benjamin", "Asher", "Robert", "Oliver", "Ezekiel", "Maverick", "Andrew", "Elijah", "James", "Zachary", "Owen", "Sebastian", "Caleb", "David", "Miles", "Carter", "Eli", "Sebastian", "Isaac", "Wyatt", "Jack", "Andrew", "Gabriel", "Matthew", "Grayson", "David", "Lucas", "Ezekiel", "Adam", "Elijah", "Maverick", "Mason", "Thomas", "Elijah", "Asher", "Sebastian", "Xavier", "Lucas", "Carter", "Hudson", "Zane", "Cameron", "Benjamin", "Levi", "William", "Lucas", "Eli", "Maxwell", "Hudson", "Landon", "Levi", "Roman", "Santiago", "Milo", "Maverick", "Carter", "Liam", "Caden", "Isaiah", "Samuel", "Ryan", "Jack", "Joshua", "Jameson", "Jacob", "Michael", "Luca", "Levi", "Asher", "Nicholas", "Caleb", "Eli", "Miles", "Wyatt", "Ezra", "Ryan", "Sebastian", "Mason", "Nolan", "Elijah", "Isaac", "Jackson", "Carter", "Gabriel", "Lucas", "Leo", "Isaiah", "Julian", "Jack", "Levi", "Mason", "Oliver", "Hudson", "Evan", "Hudson", "Noah", "Sebastian", "David", "Milo", "Aiden", "Zachary", "Blake", "Ezekiel", "Maverick", "Samuel", "Julian", "Santiago", "Xander", "Liam", "Jacob", "Adrian", "Caleb", "Jacob", "David", "Lucas", "Maverick", "Miles", "Eli", "Ethan", "Daniel", "Hudson", "Noah", "Zachary", "Owen", "Nolan", "Elijah", "Isaac", "Hudson", "Ezra", "Hunter", "Wyatt", "Eli", "Aiden", "Sebastian", "Caleb", "Jameson", "Eli", "Maverick", "Asher", "Jaxon", "Noah", "Ezekiel", "Lucas", "Roman", "Asher", "Carter", "Ezra", "Benjamin", "Hudson", "Zachary", "Sebastian", "Maverick", "Isaac", "James", "Noah", "Luke", "Jack", "Levi", "Aiden", "Jacob", "Mason", "Carter", "Wyatt", "Lucas", "Maverick", "Hudson", "Levi", "Sebastian", "David", "Santiago", "Jameson", "Lucas", "Leo", "Caden", "Hudson", "Julian", "Miles", "Zachary", "Cameron", "Isaiah", "Hudson", "Maverick", "Levi", "Mason", "Sebastian", "Blake", "Wyatt", "Ezra", "Zachary","Balls",""])
                author = f"{author} {author2}"
                id += 1
                adding = (book,author,id)
                library.add(adding)
                
            input("\nPress enter to continue")

        elif choice == 6: # Renaming Library
            cs()
            print(f"Renaming {library_name}!")
            library_name = input("Choose a name for your library!: ")
            input("Press enter to continue")
        elif choice == 7: # Print out the entire library
            cs()
            print(f"======= {library_name} =======\n")
            for x in library: # Printing out the whole library
                print(f"Book: {x[0]}") # Indexing the tuple in the set for book/author
                print(f"Author: {x[1]}")
                print(f"ID: {x[2]}\n")
            input('Press enter to continue')
        elif choice == 8: # Exit Choice
            print(f"\nExiting {library_name}! See you next time!")
            exit()

def add_item(): # Add function
    global id
    cs()
    print("Adding Item")
    book = str_input("What is the title of the book?: ")
    author = str_input("What is the authors name?: ")
    id += 1
    adding = (book,author,id) # Ordered Tuple for adding to library set
    library.add(adding) # Adds book and title 
    print(f"This book has an ID of {id}")
    input("Press enter to continue")

def remove_item(): # Remove function
    cs()
    print("Removing Item")
    search = input("Enter book or author name or ID: ")
    print()
    for x in library: # Searching for book
        for i in range(3):
            if str(x[i]) == search:
                check = 0
                print(f"Book: {x[0]}") # printing found book
                print(f"Author: {x[1]}")
                print(f"ID: {x[2]}\n")
                break
            else:
                check = 1
    if check != 1:
        deleting = int_input("Enter the ID of the item you want to remove: ")
        for x in library: # Searching for book
            if x[2] == deleting:
                library.remove(x)
                print(f"\nRemoved {x[0]} by {x[1]} with an ID of {x[2]}\n")
                break
    else:
        print("No results found!")
    input("Press enter to continue")

def search_library():
    cs()
    print(f'{library_name} Search System')
    search = input("Enter book or author full name or ID: ")
    print()
    for x in library: # Searching for book
        for i in range(3):
            if str(x[i]).lower() == search.lower():
                print(f"Book: {x[0]}") # printing found book
                print(f"Author: {x[1]}")
                print(f"ID: {x[2]}\n")
                break
    input("\nPress enter to continue")


main() 