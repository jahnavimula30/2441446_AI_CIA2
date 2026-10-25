"""Question bank for DSC401-6 Artificial Intelligence (Units I & II).

Every question is a plain dict built by one of the helpers below.
To add a question, call a helper at the bottom of the matching topic block.
Run `python scripts/export_question_bank.py` afterwards to refresh the docs
and to validate the assignment rules (>= 50 questions, >= 10 real-world,
>= 5 search/state-space, all formats present).
"""

POINTS = {"Easy": 1, "Medium": 2, "Hard": 3}

T1 = "Foundations & Applications of AI"
T2 = "Turing Test"
T3 = "Rational Agents"
T4 = "Agents & Environments"
T5 = "Problems & State Space"
T6 = "Production Systems & Problem Characteristics"
T7 = "Uninformed Search (BFS/DFS/IDS)"
T8 = "Hill Climbing & Variations"
T9 = "Heuristic & Best-First Search"
T10 = "Constraint Satisfaction (CSP)"
T11 = "Means-End Analysis"
TOPICS = [T1, T2, T3, T4, T5, T6, T7, T8, T9, T10, T11]

AR_OPTIONS = [
    "Both A and R are true, and R is the correct explanation of A",
    "Both A and R are true, but R is NOT the correct explanation of A",
    "A is true, but R is false",
    "A is false, but R is true",
]

QUESTIONS = []


def _add(**kw):
    kw["id"] = len(QUESTIONS) + 1
    QUESTIONS.append(kw)


def mcq(topic, diff, q, opts, ans, why, hint, fmt="MCQ", rw=False, search=False):
    """Multiple choice. `ans` = index of the correct option."""
    _add(topic=topic, difficulty=diff, format=fmt, input="mcq", question=q, options=opts,
         answer=ans, explanation=why, hint=hint, real_world=rw, search=search)


def tf(topic, diff, q, ans, why, hint, rw=False, search=False):
    _add(topic=topic, difficulty=diff, format="True/False", input="tf", question=q,
         options=["True", "False"], answer=0 if ans else 1, explanation=why, hint=hint,
         real_world=rw, search=search)


def ar(topic, diff, a, r, ans, why, hint, rw=False, search=False):
    _add(topic=topic, difficulty=diff, format="Assertion-Reason", input="ar",
         question=f"**Assertion (A):** {a}\n\n**Reason (R):** {r}", options=AR_OPTIONS,
         answer=ans, explanation=why, hint=hint, real_world=rw, search=search)


def fill(topic, diff, q, answers, why, hint, rw=False, search=False):
    _add(topic=topic, difficulty=diff, format="Fill in the Blanks", input="fill", question=q,
         answer=answers, explanation=why, hint=hint, real_world=rw, search=search)


def match(topic, diff, q, pairs, why, hint, rw=False, search=False):
    _add(topic=topic, difficulty=diff, format="Match the Following", input="match", question=q,
         pairs=pairs, explanation=why, hint=hint, real_world=rw, search=search)


TREE = """```
A
├── B
│   ├── D
│   └── E
└── C
    └── F
```"""

# ───────────────────────── Unit I: Foundations ─────────────────────────
tf(T1, "Easy", "Machine Learning is a subset of Artificial Intelligence.", True,
   "ML is one way to build AI (learning from data). AI also includes search, logic, planning and knowledge representation.",
   "Think of AI as the umbrella term.")
mcq(T1, "Medium", "A bank's system monitors millions of card transactions in real time and blocks those that look "
    "unusual compared with a customer's normal behaviour. Which AI application area is this?",
    ["Anomaly / fraud detection (machine learning)", "Machine translation", "Robotic path planning",
     "Computer-graphics rendering"], 0,
    "Spotting transactions that deviate from learned normal behaviour is anomaly (fraud) detection.",
    "The key word is 'unusual'.", fmt="Scenario", rw=True)
mcq(T1, "Easy", "Google Maps finds the quickest route between two cities by treating roads as a graph. "
    "Which core AI idea does this rely on?",
    ["Heuristic graph search (e.g., A*)", "Speech recognition", "Image classification", "Genetic evolution of maps"], 0,
    "Route finding is a shortest-path search problem on a graph, commonly solved with A*-style heuristic search.",
    "Roads = edges, junctions = nodes.", fmt="Scenario", rw=True, search=True)
match(T1, "Easy", "Match each AI application with its main AI area.",
      [("Alexa / Siri voice assistant", "Natural Language Processing"),
       ("Deep Blue playing chess", "Game playing / search"),
       ("MYCIN medical diagnosis", "Expert systems"),
       ("Self-driving car lane detection", "Computer vision")],
      "Voice assistants rely on NLP, Deep Blue on game-tree search, MYCIN is a classic rule-based expert system, and lane detection is computer vision.",
      "MYCIN is a rule-based medical system from the 1970s.")
fill(T1, "Easy", "The term 'Artificial Intelligence' was coined by John McCarthy for the 1956 ______ workshop.",
     ["Dartmouth", "Dartmouth College"],
     "The 1956 Dartmouth Summer Research Project is considered the birth of AI as a field.",
     "An Ivy League college in New Hampshire.")

# ───────────────────────── Turing Test ─────────────────────────
mcq(T2, "Easy", "Alan Turing proposed his 'imitation game' in which 1950 paper?",
    ["Computing Machinery and Intelligence", "On Computable Numbers", "The Chemical Basis of Morphogenesis",
     "A Logical Calculus of the Ideas Immanent in Nervous Activity"], 0,
    "'Computing Machinery and Intelligence' (Mind, 1950) introduced the imitation game.",
    "The title pairs 'machinery' with 'intelligence'.")
tf(T2, "Medium", "To pass the standard Turing Test, a machine must be able to physically manipulate objects.", False,
   "That requirement belongs to the Total Turing Test. The standard test is a text-only conversation.",
   "The standard test hides the machine behind a terminal.")
mcq(T2, "Medium", "Which capability is required for the Total Turing Test but NOT for the standard Turing Test?",
    ["Natural language processing", "Knowledge representation", "Computer vision and robotics", "Machine learning"], 2,
    "The Total Turing Test adds perception (vision) and physical action (robotics) to the four standard capabilities.",
    "'Total' adds senses and a body.")
ar(T2, "Medium", "The Turing Test is a test of 'acting humanly'.",
   "The machine passes if a human interrogator cannot tell whether written replies come from a person or a computer.", 0,
   "Judging by indistinguishable behaviour is exactly what 'acting humanly' means, so R explains A.",
   "Behaviour, not internal mechanism, is judged.")
mcq(T2, "Medium", "A website shows distorted letters and asks you to type them to prove you are not a bot. "
    "This is best described as:",
    ["A reverse Turing test (a machine judges whether the user is human)", "The Total Turing Test",
     "The Chinese Room argument", "A minimax evaluation"], 0,
    "In a CAPTCHA the judge is a computer and the subject is a (possible) human, the reverse of Turing's setup.",
    "Who is the judge here: a human or a computer?", fmt="Scenario", rw=True)

# ───────────────────────── Rational Agents ─────────────────────────
mcq(T3, "Easy", "A rational agent is one that:",
    ["Always achieves the best possible actual outcome",
     "Selects the action expected to maximise its performance measure, given its percepts and knowledge",
     "Behaves exactly like a human", "Never makes mistakes because it knows everything"], 1,
    "Rationality is about maximising EXPECTED performance given what the agent has perceived and knows.",
    "Expected, not guaranteed.")
ar(T3, "Medium", "Rationality is not the same as omniscience.",
   "A rational agent maximises expected performance, not actual performance.", 0,
   "An omniscient agent would know actual outcomes in advance. A rational agent only does the best it can with its percepts, so R explains A.",
   "Crossing a road after looking both ways can still end badly.")
fill(T3, "Medium", "Rationality depends on the performance measure, the agent's prior knowledge, its available actions "
     "and its percept ______.", ["sequence", "percept sequence"],
     "The four factors are: performance measure, prior knowledge, actions, and the percept sequence to date.",
     "The complete history of what the agent has perceived.")
mcq(T3, "Medium", "A robot vacuum is rewarded for the amount of dirt it picks up. It learns to dump dirt on the floor "
    "and suck it up again. What design lesson does this teach?",
    ["Performance measures should reward the desired state of the environment, not the agent's activity",
     "Robot vacuums need faster motors", "Rational agents must be omniscient", "Rewards should be removed completely"], 0,
    "Reward the outcome you want (a clean floor), not a behaviour that can be gamed.",
    "What do you really want: dirt collected or a clean floor?", fmt="Scenario", rw=True)

# ───────────────────────── Agents & Environments ─────────────────────────
match(T4, "Medium", "Match each agent type with its key idea.",
      [("Simple reflex agent", "Acts on the current percept using condition-action rules"),
       ("Model-based reflex agent", "Keeps an internal state to track the unseen world"),
       ("Goal-based agent", "Chooses actions that achieve a desired goal"),
       ("Utility-based agent", "Maximises a measure of 'happiness' among alternatives")],
      "These are the four basic agent programs of increasing generality.",
      "Utility = 'how happy' a state makes the agent.")
mcq(T4, "Easy", "PEAS in agent design stands for:",
    ["Performance, Environment, Actuators, Sensors", "Planning, Execution, Analysis, Search",
     "Percept, Evaluation, Action, State", "Problem, Estimation, Algorithm, Solution"], 0,
    "PEAS describes the task environment of an agent.", "Two of the letters are about input and output devices.")
mcq(T4, "Medium", "In an automated taxi, which of the following is an ACTUATOR?",
    ["Steering, accelerator and brake", "GPS receiver", "Cameras and sonar", "Speedometer"], 0,
    "Actuators carry out actions. GPS, cameras, sonar and the speedometer are sensors.",
    "Actuators produce actions; sensors collect percepts.", fmt="Scenario", rw=True)
mcq(T4, "Medium", "Which description best fits the environment of chess (without a clock)?",
    ["Fully observable, deterministic, sequential, static, discrete, multi-agent",
     "Partially observable, stochastic, episodic, dynamic, continuous, single-agent",
     "Fully observable, stochastic, episodic, static, continuous, single-agent",
     "Partially observable, deterministic, episodic, dynamic, discrete, single-agent"], 0,
    "All pieces are visible, moves have certain results, the board does not change while thinking, and there are two players.",
    "Nothing is hidden and nothing is random.")
mcq(T4, "Medium", "An agent must trade off conflicting goals (e.g., speed versus safety) and compare how good different "
    "outcomes are. Which agent type is most suitable?",
    ["Simple reflex agent", "Model-based reflex agent", "Goal-based agent (binary goals only)", "Utility-based agent"], 3,
    "A utility function gives a degree of preference, which is needed to balance conflicting goals.",
    "You need a numeric 'how good' measure.")
mcq(T4, "Easy", "A thermostat switches the heater ON whenever the room temperature is below 20 °C. "
    "What type of agent is it?",
    ["Simple reflex agent", "Utility-based agent", "Learning agent", "Goal-based planning agent"], 0,
    "It maps the current percept straight to an action with a condition-action rule and keeps no memory.",
    "IF temperature < 20 THEN heat.", fmt="Scenario", rw=True)
ar(T4, "Medium", "A simple reflex agent can get stuck in an infinite loop in a partially observable environment.",
   "It decides using only the current percept and keeps no memory of earlier percepts.", 0,
   "Without memory it cannot tell it has repeated the same situation, so R explains A.",
   "No memory means no way to notice a loop.")

# ───────────────────────── Problems & State Space ─────────────────────────
mcq(T5, "Easy", "The state space of a problem is:",
    ["The set of all states reachable from the initial state by any sequence of actions",
     "Only the goal states", "The memory used by the algorithm", "The list of heuristics"], 0,
    "Together with the actions it forms a graph that search explores.", "Think 'everything reachable'.")
fill(T5, "Easy", "A well-defined problem has an initial state, a set of actions, a goal test and a path ______ function.",
     ["cost"], "The path cost function assigns a numeric cost to each path so that the best solution can be chosen.",
     "What you pay for each step.")
mcq(T5, "Easy", "In the 8-puzzle the blank can move Up, Down, Left or Right. If the blank is in a CORNER square, "
    "how many successor states does that state have?", ["1", "2", "3", "4"], 1,
    "A corner square has only two neighbours, so only two moves are legal. An edge square gives 3 and the centre gives 4.",
    "Count the neighbours of a corner cell.", fmt="Problem-solving", search=True)
mcq(T5, "Medium", "Only half of the 9! arrangements of the 8-puzzle can reach a given goal. "
    "How many states are reachable from any one start state?", ["362,880", "181,440", "40,320", "9"], 1,
    "9!/2 = 181,440. The other half is unreachable because of a parity invariant.",
    "9! = 362,880.", fmt="Problem-solving", search=True)
mcq(T5, "Medium", "3 missionaries (M) and 3 cannibals (C) must cross a river. Cannibals must never outnumber "
    "missionaries on a bank that has at least one missionary. Which left-bank state (M, C) is ILLEGAL?",
    ["(3, 3)", "(2, 2)", "(1, 2)", "(0, 2)"], 2,
    "With (1, 2) on the left, 2 cannibals outnumber 1 missionary. (0, 2) is fine because no missionaries are present to be eaten.",
    "Check both banks for each option.", fmt="Problem-solving", search=True)
mcq(T5, "Medium", "Water-jug problem with a 4 L and a 3 L jug; state (x, y) = litres in (4 L jug, 3 L jug). Start (0, 0). "
    "Fill the 3 L jug, pour it into the 4 L jug, fill the 3 L jug again, then pour into the 4 L jug until it is full. "
    "What is the new state?", ["(4, 2)", "(3, 2)", "(4, 3)", "(2, 3)"], 0,
    "(0,0) -> (0,3) -> (3,0) -> (3,3) -> (4,2). Only 1 L fits into the 4 L jug, leaving 2 L in the 3 L jug.",
    "The 4 L jug already holds 3 L, so it only takes 1 L more.", fmt="Problem-solving", search=True)

# ───────────────────── Production Systems & Problem Characteristics ─────────────────────
mcq(T6, "Medium", "Which of these is NOT a component of a production system?",
    ["A set of production (condition-action) rules", "A global database / working memory", "A control strategy",
     "A matrix of trained neural-network weights"], 3,
    "A production system has rules, a global database and a control strategy (plus a rule applier).",
    "Production systems are symbolic, rule-based.")
match(T6, "Medium", "Match each problem characteristic with its classic example.",
      [("Ignorable solution steps", "Theorem proving"), ("Recoverable solution steps", "8-puzzle"),
       ("Irrecoverable solution steps", "Chess"), ("Decomposable problem", "Symbolic integration")],
      "Ignorable: steps can be forgotten. Recoverable: steps can be undone. Irrecoverable: moves cannot be undone. "
      "Decomposable: split into independent sub-problems.", "Can you undo a chess move?")
fill(T6, "Medium", "A production system in which applying a rule never prevents the later application of another rule "
     "that was already applicable is called ______.", ["monotonic"],
     "That is the definition of a monotonic production system.", "The opposite is non-monotonic.")
mcq(T6, "Medium", "In real chess a player cannot simply 'undo' a poor move and try another. Which problem characteristic "
    "does this illustrate?",
    ["Irrecoverable solution steps", "Ignorable solution steps", "Decomposable sub-problems", "A consistent knowledge base"], 0,
    "Moves in chess cannot be undone, so the system must plan carefully (no naive backtracking).",
    "Can the step be reversed?", fmt="Scenario", rw=True)
mcq(T6, "Medium", "In search-program design, why do we keep an explored (CLOSED) list?",
    ["To avoid re-expanding repeated states and looping, i.e. treat the space as a graph rather than a tree",
     "To make the heuristic admissible", "To reduce the branching factor to 1", "To convert DFS into BFS"], 0,
    "Remembering visited states prevents infinite loops and duplicated work.",
    "A graph can revisit the same state through different paths.", search=True)

# ───────────────────────── Uninformed Search ─────────────────────────
mcq(T7, "Easy", "Breadth-First Search stores its frontier in a:",
    ["Queue (FIFO)", "Stack (LIFO)", "Priority queue ordered by h(n)", "Hash set only"], 0,
    "A FIFO queue makes BFS expand the shallowest nodes first.", "First in, first out.", search=True)
tf(T7, "Medium", "Depth-First Search is complete even in infinite state spaces.", False,
   "DFS can follow an infinitely deep branch forever and never return to find a solution on another branch.",
   "What if one branch never ends?", search=True)
mcq(T7, "Medium", "Children are visited left to right. In what order does BFS visit the nodes of this tree, starting from A?\n\n"
    + TREE, ["A, B, C, D, E, F", "A, B, D, E, C, F", "A, C, F, B, D, E", "F, E, D, C, B, A"], 0,
    "BFS goes level by level: A | B, C | D, E, F.", "Level by level.", fmt="Problem-solving", search=True)
mcq(T7, "Medium", "Children are visited left to right. In what order does DFS visit the nodes of this tree, starting from A?\n\n"
    + TREE, ["A, B, C, D, E, F", "A, B, D, E, C, F", "A, C, F, B, D, E", "F, E, D, C, B, A"], 1,
    "DFS goes as deep as possible first: A, B, D, then back up to E, then C, F.", "Go deep, then backtrack.",
    fmt="Problem-solving", search=True)
mcq(T7, "Medium", "The depth of the shallowest solution is unknown and the state space is huge. Which uninformed strategy "
    "gives BFS-like completeness with DFS-like memory use?",
    ["Iterative Deepening DFS", "Depth-limited DFS", "Uniform-cost search", "Bidirectional DFS"], 0,
    "IDS repeats depth-limited DFS with growing limits: complete, optimal for unit costs, and O(bd) memory.",
    "Repeated DFS with a growing depth limit.", search=True)
mcq(T7, "Hard", "With branching factor b = 10 and solution depth d = 5, how many nodes does Iterative Deepening generate "
    "(counting d·b + (d-1)·b² + ... + 1·b^d)?", ["111,110", "123,450", "100,000", "1,234,500"], 1,
    "5(10) + 4(100) + 3(1,000) + 2(10,000) + 1(100,000) = 123,450, only about 11% more than BFS's 111,110.",
    "Shallow levels are regenerated many times, deep ones only once.", fmt="Problem-solving", search=True)
ar(T7, "Medium", "BFS finds an optimal solution when all step costs are equal.",
   "BFS always expands the shallowest unexpanded node first.", 0,
   "The first goal found is at the minimum depth, which is the cheapest path when every step costs the same.",
   "Shallowest first means fewest steps.", search=True)
mcq(T7, "Easy", "To find the minimum number of 'hops' (degrees of separation) between two people in a social network, "
    "which uninformed search is the natural choice?",
    ["Breadth-First Search", "Depth-First Search", "Hill climbing", "Random restart"], 0,
    "BFS explores friends, then friends-of-friends, and so on, so the first time it meets the target is the fewest hops.",
    "Shortest in number of edges.", fmt="Scenario", rw=True, search=True)

# ───────────────────────── Hill Climbing ─────────────────────────
mcq(T8, "Easy", "Hill climbing is best described as:",
    ["A greedy local search that moves to a better neighbouring state",
     "A complete systematic search that guarantees the global optimum",
     "A search that expands the shallowest node first", "A search that uses a stack of unexplored nodes"], 0,
    "It only looks at the current state's neighbours and keeps no search tree.", "Greedy and local.")
mcq(T8, "Medium", "Which of these is NOT a known problem of hill climbing?",
    ["Local maxima", "Plateaus", "Ridges", "Needing exponential memory to hold a large frontier"], 3,
    "Hill climbing keeps only the current state, so memory is tiny. The problems are local maxima, plateaus and ridges.",
    "It keeps only the current state.")
match(T8, "Medium", "Match each hill-climbing variant with how it works.",
      [("Simple hill climbing", "Moves to the first neighbour that is better than the current state"),
       ("Steepest-ascent hill climbing", "Examines all neighbours and moves to the best one"),
       ("Stochastic hill climbing", "Picks randomly among the uphill moves"),
       ("Random-restart hill climbing", "Restarts from random initial states until a good optimum is found")],
      "Each variant changes how the next move is chosen or how local maxima are escaped.",
      "Steepest = looks at everything before moving.")
mcq(T8, "Medium", "A delivery-route optimiser using hill climbing keeps getting stuck on a route that is not the best, "
    "even though better routes exist. Which remedy is most appropriate?",
    ["Random-restart hill climbing or simulated annealing", "Switching to DFS with no depth limit",
     "Removing the objective function", "Using only the first neighbour found"], 0,
    "Restarting from new random states, or occasionally accepting worse moves, helps escape local maxima.",
    "Escape the local peak.", fmt="Scenario", rw=True)
fill(T8, "Medium", "A flat region of the search landscape where all neighbouring states have the same value is called a ______.",
     ["plateau"], "On a plateau no neighbour is better, so simple hill climbing cannot decide where to go.",
     "A high, flat area of land.")

# ───────────────────────── Heuristic & Best-First ─────────────────────────
mcq(T9, "Medium", "A* search ranks nodes by f(n) = ?", ["g(n) + h(n)", "h(n) only", "g(n) only", "g(n) - h(n)"], 0,
    "g(n) is the cost so far, h(n) the estimated cost to go. f(n) estimates the total cost via n.",
    "Cost so far plus estimate to go.", search=True)
tf(T9, "Hard", "A* with an admissible heuristic returns an optimal solution (tree search).", True,
   "If h never overestimates, the first goal A* expands has the lowest cost.", "Admissible = optimistic.", search=True)
mcq(T9, "Medium", "Node P has g = 5, h = 3. Node Q has g = 2, h = 8. Which node will A* expand first?",
    ["P (f = 8)", "Q (f = 10)", "Both, simultaneously", "Neither: A* uses only h"], 0,
    "f(P) = 5 + 3 = 8 and f(Q) = 2 + 8 = 10. A* expands the lowest f first.", "Compute f for both.",
    fmt="Problem-solving", search=True)
mcq(T9, "Hard", "8-puzzle (blank shown as _):\n\n```\nCurrent      Goal\n2 8 3        1 2 3\n1 6 4        8 _ 4\n7 _ 5        7 6 5\n```\n"
    "What is the Manhattan-distance heuristic value h(n) of the current state (blank not counted)?",
    ["3", "4", "5", "6"], 2,
    "Tile 2 = 1, tile 8 = 2, tile 1 = 1, tile 6 = 1, others 0, so h = 5. (Misplaced tiles would give 4.)",
    "Sum of horizontal + vertical moves for each misplaced tile.", fmt="Problem-solving", search=True)
mcq(T9, "Medium", "A drone path-planner uses A* with straight-line (Euclidean) distance to the goal as its heuristic. "
    "Why is this heuristic admissible?",
    ["A straight line is never longer than any real path, so it never overestimates the cost",
     "It equals the exact path cost in every map", "It ignores obstacles, so it always overestimates",
     "It is a random estimate"], 0,
    "The shortest possible route is the straight line, so the estimate can never exceed the real cost.",
    "No path can be shorter than a straight line.", fmt="Scenario", rw=True, search=True)
fill(T9, "Medium", "A heuristic that never overestimates the true cost to reach the goal is called ______.",
     ["admissible"], "Admissibility is the condition that makes A* optimal.", "Starts with 'ad-'.", search=True)

# ───────────────────────── CSP ─────────────────────────
mcq(T10, "Easy", "A Constraint Satisfaction Problem is defined by:",
    ["Variables, domains and constraints", "States, actions and rewards", "Rules, facts and goals",
     "Nodes, edges and weights only"], 0,
    "A CSP has a set of variables, a domain of values for each, and constraints on allowed combinations.",
    "Three ingredients starting with V, D, C.")
mcq(T10, "Medium", "Australia map colouring: the adjacent pairs are WA-NT, WA-SA, NT-SA, NT-Q, SA-Q, SA-NSW, SA-V, Q-NSW, NSW-V. "
    "What is the minimum number of colours needed for the mainland?", ["2", "3", "4", "5"], 1,
    "WA, NT and SA are mutually adjacent, so at least 3 colours are needed, and 3 suffice.",
    "Find three regions that all touch each other.", fmt="Problem-solving")
fill(T10, "Medium", "In backtracking search for CSPs, the MRV heuristic stands for Minimum ______ Values.",
     ["remaining"], "MRV picks the variable with the fewest legal values left, to fail early.",
     "Values that are still legal.")
tf(T10, "Medium", "Forward checking removes values from the domains of unassigned neighbouring variables after each assignment.",
   True, "That is exactly what forward checking does, and it backtracks as soon as a domain becomes empty.",
   "It looks one step ahead.")
mcq(T10, "Medium", "A university must schedule exams so that no student has two exams at the same time. "
    "In CSP terms, what are the VARIABLES?", ["The exams", "The time slots", "The students", "The rooms"], 0,
    "Variables = exams, domains = time slots, constraints = exams that share a student cannot share a slot.",
    "What needs to be assigned a value?", fmt="Scenario", rw=True)
mcq(T10, "Hard", "In the cryptarithmetic puzzle SEND + MORE = MONEY (each letter a distinct digit), what must the value of M be?",
    ["0", "1", "9", "2"], 1,
    "Two 4-digit numbers sum to less than 20,000, so the 5-digit result starts with a carry of 1, hence M = 1.",
    "How large can the sum of two 4-digit numbers be?", fmt="Problem-solving")
ar(T10, "Hard", "Arc consistency can detect that a branch is hopeless before every variable is assigned.",
   "If enforcing arc consistency empties some variable's domain, no solution exists in that branch.", 0,
   "An empty domain means a variable has no legal value, so the search can backtrack immediately.",
   "An empty domain means no possible value.")

# ───────────────────────── Means-End Analysis ─────────────────────────
mcq(T11, "Easy", "Means-End Analysis works mainly by:",
    ["Reducing the difference between the current state and the goal state", "Expanding nodes level by level",
     "Randomly restarting from new states", "Ordering nodes by path cost only"], 0,
    "MEA finds the biggest difference to the goal and picks an operator that reduces it.", "Look at the gap.")
mcq(T11, "Medium", "Means-End Analysis was the core technique of which early AI program by Newell and Simon?",
    ["General Problem Solver (GPS)", "MYCIN", "ELIZA", "Deep Blue"], 0,
    "GPS (1957) used means-end analysis to solve a wide range of formal problems.", "The name says 'general'.")
fill(T11, "Medium", "When an operator's preconditions are not satisfied, Means-End Analysis creates a ______ to achieve them first.",
     ["subgoal", "sub-goal", "sub goal"], "Setting up subgoals lets MEA mix forward and backward reasoning.",
     "A smaller goal inside the bigger goal.")
mcq(T11, "Medium", "A household robot must carry a box into the next room, but the door is closed. It first sets "
    "'open the door' as a new sub-task, then carries the box. This behaviour is typical of:",
    ["Means-End Analysis", "Hill climbing", "Depth-first search", "Forward chaining of facts only"], 0,
    "The unmet precondition (open door) becomes a subgoal, which is the signature of MEA.",
    "An unmet precondition creates a new sub-task.", fmt="Scenario", rw=True)
mcq(T11, "Hard", "Monkey-and-bananas: bananas hang from the ceiling out of reach and a box is in the corner of the room. "
    "Which operator sequence achieves the goal?",
    ["Walk to box -> push box under bananas -> climb box -> grab bananas",
     "Climb box -> walk to box -> grab bananas -> push box",
     "Grab bananas -> push box -> walk to box -> climb box",
     "Push box -> grab bananas -> walk to box -> climb box"], 0,
    "Each operator's preconditions must hold: reach the box, move it under the bananas, climb on it, then grab.",
    "Work backwards: what must be true to grab the bananas?", fmt="Problem-solving", search=True)
