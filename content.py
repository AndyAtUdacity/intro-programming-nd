from google.appengine.ext import ndb

DEFAULT_GUESTBOOK_NAME = 'default_guestbook'
DEFAULT_CODE_EXAMPLES_NAME = 'default_code_examples'
DEFAULT_CODE_PEN_NAME = 'default_code_pen'
COURSES = [
	{"title"    : "Webpages, Documents, and Structure",
		"description" : ("This was my introduction to the world of coding. "
										 "I wrote some simple HTML and CSS to make static web "
										 "pages. I was first introduced to the principle of "
										 "'Don't Repeat Yourself' in this course when I started "
										 "using HTML classes and CSS styling to make similar HTML "
										 "elements look the same."),
		"url" : "https://www.udacity.com/course/viewer#!/c-ud721-nd/",
		"favorite_video": {
			"title"   : "Interview with Jacques",
			"url"     : "https://www.youtube.com/embed/Nj5RCaE_b00",
			"caption" : "Jacques, A professional front-end web developer, explains how he 'boxifies' designs."
		},
		"lessons" : [
			{
			"title"     : "The Basics of the Web and HTML",
			"description"  : "The internet is a bunch of computers communicating over HTTP",
			"url" : "https://www.udacity.com/course/viewer#!/c-ud721-nd/l-3508959201",
			"concepts" : [
					{	"title" 			: "HTML",
					 	"description" : "HyperText Markup Language"},
					{	"title" 			: "Elements",
						"description" : "HTML documents are made up of HTML 'elements'."
					}
				]
			},
			{
			"title"			: "Creating a Structured Document with HTML",
			"description"   : "How elements within elements creates a structured 'box-like' model of a web page.",
			"url" : "https://www.udacity.com/course/viewer#!/c-ud721-nd/l-3555039510",
			"concepts"  : [
					{ "title"				: "Divs and Spans",
						"description" : "These are the two 'container' elements that can be used to build the structure of a web page."},
					{ "title"				: "Box Model",
						"description" : "Everything on the web is boxes!"
					}
				]
			},
			{
			"title"			: "Adding CSS Style to HTML Structure",
			"description"   : "By giving similar HTML elements the same 'class', we can write all the styling for that class just ONCE and it will apply to every element. ",
			"url" : "https://www.udacity.com/course/viewer#!/c-ud721-nd/l-3575138706",
			"concepts"  : [
					{ "title"				: "Style",
						"description" : "The 'style' of an HTML element is just a bunch of rules which describe how that element should look. This style can be specified in a CSS file."},
					{ "title"				: "Avoiding Repetition",
						"description" : "It's good to avoid repetition when programming. If you give the same style to similar elements, you can reap the benefits of this when you quickly and easily modify all of them at once just by changing a single line of CSS."
					}
				]
			}
		]
	},
	{ "title"    : "Telling Computers what to do",
		"description" : ("I learned the programming basics: variables, functions "
										 "various data types (strings, numbers, lists...), etc... "
										 "This course was definitely hard and I still don't feel "
										 "like an expert in solving problems with Python, but I "
										 "can at least read and reuse other people's code if I want to. "),
		"url" : "https://www.udacity.com/course/viewer#!/c-ud552-nd",
		"favorite_video": {
			"title"   : "Making vs Using Functions",
			"url"     : "https://www.youtube.com/embed/JJBo7mfgoTs",
			"caption" : "A review of Python functions as well as a good explanation of the difference between making and using functions."
		},
		"lessons" : [
			{
			"title"     : "Introduction to Serious Programming",
			"description"  : "Big Problems can be broken into smaller pieces.",
			"url" : "https://www.udacity.com/course/viewer#!/c-ud552-nd/l-3527838955",
			"concepts" : [
					{	"title" 			: "Computer",
					 	"description" : "A computer is a machine that can carry out instructions given to it by a programmer."},
					{	"title" 			: "Grammar",
						"description" : "Grammar refers to the rules that govern what statements are 'legal' in a language. Python has it's own grammar."
					}
				]
			},
			{
			"title"			: "Variables and Strings",
			"description"   : "We can store textual information (strings) in titled containers (variables)",
			"url" : "https://www.udacity.com/course/viewer#!/c-ud552-nd/l-3574398630",
			"concepts"  : [
					{ "title"				: "Variable",
						"description" : "A variable is a titled container that holds information. "},
					{ "title"				: "String",
						"description" : "A string is just text. We create strings by using single or double quotes."
					}
				]
			},
			{
			"title"			: "Input --> Function --> Output",
			"description"   : "A function is something that takes input, does something with that input, and then returns something else as output.",
			"url" : "https://www.udacity.com/course/viewer#!/c-ud552-nd/l-3574398630",
			"concepts"  : [
					{ "title"				: "Defining Functions",
						"description" : "In Python, functions are defined by writing the 'def' keyword followed by a name, and then the 'parameters' for the function (inside parentheses), and a colon."},
					{ "title"				: "return vs print",
						"description" : "When functions don't have a 'return' statement, they don't really do anything (even though they may print out some text). You usually want to make sure to end your function with a return statement."
					}
				]
			},
			{
			"title"			: "Decisions and Repetition - If and While",
			"description"   : "Control flow statements (like 'if' and 'else') let us execute different blocks of code depending on some condition. While loops let us repeat a certain block of code many times until a certain condition is met.",
			"url" : "https://www.udacity.com/course/viewer#!/c-ud552-nd/l-3574398630",
			"concepts"  : [
					{ "title"				: "==, !=, >, <, >=, <=",
						"description" : "These are all Python 'comparison operators'. They return the 'boolean' True when they are correct and False when they aren't. For example, 5 != 6 would return True, since 5 is not equal to 6."},
					{ "title"				: "if, then, else",
						"description" : "These three Python keywords let us tell Python what code we want it to execute in different situations."},
					{ "title"				: "while loops",
						"description" : "A while loop will repeat the indented block of code beneath it as long as the condition on the first line (right after 'while') is true."
					}
				]
			}
		]
	},
	{ "title"    : "The Power of Abstraction",
		"description" : ("This course taught me how to avoid repetition "
										 "in my code by defining 'Classes' of 'Objects' with "
										 "similar properties. This 'Object-Oriented' style of "
										 "programming also lets me think about programs in a "
										 "way that I'm familiar with"),
		"url" : "https://www.udacity.com/course/viewer#!/c-ud645-nd",
		"favorite_video": {
			"title"   : "Vocabulary Recap",
			"url"     : "https://www.youtube.com/embed/11G5sBkY9tQ",
			"caption" : "A review of important vocabulary from the course like class, instance, constructor, instance variables, instance methods, and self."
		},
		"lessons" : [
			{
			"title"     : "Use Functions",
			"description"  : "A review of functions in Python.",
			"url" : "https://www.udacity.com/course/viewer#!/c-ud645-nd/l-3579538661",
			"concepts" : [
					{	"title" 			: "Computer",
					 	"description" : "A computer is a machine that can carry out instructions given to it by a programmer."},
					{	"title" 			: "Grammar",
						"description" : "Grammar refers to the rules that govern what statements are 'legal' in a language. Python has it's own grammar."
					}
				]
			},
			{
			"title"			: "Use Classes - Draw Turtles",
			"description"   : "Learn how to use Python 'classes' which other programmers have already written.",
			"url" : "https://www.udacity.com/course/viewer#!/c-ud645-nd/l-3525629753",
			"concepts"  : [
					{ "title"				: "Variable",
						"description" : "A variable is a titled container that holds information. "},
					{ "title"				: "String",
						"description" : "A string is just text. We create strings by using single or double quotes."
					}
				]
			},
			{
			"title"			: "Use Classes - Send Text",
			"description"   : "Use 'Twillio' to send text messages to people with code!",
			"url" : "https://www.udacity.com/course/viewer#!/c-ud645-nd/l-3524089779",
			"concepts"  : [
					{ "title"				: "External Libraries",
						"description" : "An 'external library' is just a library that someone has written that does not come packaged with Python (Twillio is an example)."},
					{ "title"				: "from __ import __",
						"description" : "When you write something like 'from twillio.rest import TwilioRestClient', you gain access to TwilioRestClient without having to import all the extra stuff that is in twillio.rest."
					}
				]
			},
			{
			"title"			: "Use Classes - Profanity Editor",
			"description"   : "Learn about how to work with files while making a profanity editor.",
			"url" : "https://www.udacity.com/course/viewer#!/c-ud645-nd/l-3486659368",
			"concepts"  : [
					{ "title"				: "Reading Documentation",
						"description" : "Since there are SO many tools out there for programmers to use, a big part of programming is finding and learning how to use the right ones. Reading the documentation for the tools you use is VERY important."},
					{ "title"				: "Built-in Functions",
						"description" : "Python has a lot of built-in functions. These functions usually do something that is widely useful to many people. My favorite built-in function is 'enumerate'."
					}
				]
			},
			{
			"title"			: "Make Classes - Movie Website",
			"description"   : "Learn how to make your own Python 'classes' and build a website that displays movie information.",
			"url" : "https://www.udacity.com/course/viewer#!/c-ud645-nd/l-3567738950/",
			"concepts"  : [
					{ "title"				: "Class vs Instance",
						"description" : "A 'Class' is like a blueprint for a building while an 'instance' is like an ACTUAL building that was made from the blueprint."},
					{ "title"				: "Instance Methods",
						"description" : "Instance methods are special functions that belong to an 'instance' of a 'class.' They usually get or set information about the instance they are attached to."
					}
				]
			},
			{
			"title"			: "Make Classes - Advanced Topics",
			"description"   : "Learn about topics like Class methods, Inheritance, and Method Overriding.",
			"url" : "https://www.udacity.com/course/viewer#!/c-ud645-nd/l-3572248644",
			"concepts"  : [
					{ "title"				: "Inheritance",
						"description" : "When you use inheritance, you figure out what seemingly different things have in common and then capture that commonality in a 'parent' class."},
					{ "title"				: "Inheritance Example",
						"description" : "In this lesson, we realized that instances of the TvShow class have a lot in common with instances of the Movie class. We put the common elements into a new Video class and had Movie and TvShow inherit from Video."
					}
				]
			}
		]
	},
	{ "title"    : "The Full Stack",
		"description" : ("This course taught me how to actually make a web page! "
										 "I learned about and wrote 'server-side' code and used "
										 "Google AppEngine to host my page."),
		"url" : "https://www.udacity.com/course/viewer#!/c-ud645-nd",
		"favorite_video": {
			"title"   : "Handling HTML Input",
			"url"     : "https://www.youtube.com/embed/K37Ldm4GSPo",
			"caption" : "A great explanation of why it's so important to properly handle user input (and the bad things that could happen if we don't)."
		},
		"lessons" : [
			{
			"title"     : "Introduction to Networks",
			"description"  : "Networks (like the internet) are made of a bunch of links between 'nodes'. Information can be sent on a network by passing it from node to node until it reaches its destination.",
			"url" : "https://www.udacity.com/course/viewer#!/c-ud744-nd/l-3550189560",
			"concepts" : [
					{	"title" 			: "Computer",
					 	"description" : "A computer is a machine that can carry out instructions given to it by a programmer."},
					{	"title" 			: "Grammar",
						"description" : "Grammar refers to the rules that govern what statements are 'legal' in a language. Python has it's own grammar."
					}
				]
			},
			{
			"title"			: "Make the Internet Work for You",
			"description"   : "When you type a URL into your browser and hit Enter, a 'request' gets sent to a server. The server handles that request and sends back a 'response'.",
			"url" : "https://www.udacity.com/course/viewer#!/c-ud744-nd/l-3494188878",
			"concepts"  : [
					{ "title"				: "Variable",
						"description" : "A variable is a titled container that holds information. "},
					{ "title"				: "String",
						"description" : "A string is just text. We create strings by using single or double quotes."
					}
				]
			}
		]
	}
	]
# THINKING = [
# 	{"title" : "Abstract Thinking",
# 		"description" : ("Abstract thinking means finding similarity, or as "
# 						 "programmers would say, generality amongst seemingly "
# 						 "different things."),
# 		"examples" : [
# 			{"title" : "title-1",
# 			 "description" : "description-1"},
# 			{"title" : "title-2",
# 			 "description" : "description-2"}
# 		]
# 	},
# 	{"title" : "Procedural Thinking",
# 		"description" : ("Procedural thinking involves creating perfectly "
# 						 "clear and unambiguous instructions for a computer "
# 						 "to follow."),
# 		"examples" : [
# 			{"title" : "title-1",
# 			 "description" : "description-1"},
# 			{"title" : "title-2",
# 			 "description" : "description-2"}
# 		]
# 	},
# 	{"title" : "Systems Thinking",
# 		"description" : ("Systems thinking happens when you break a big "
# 						 "problem down into smaller pieces. Programmers do "
# 						 "this when they create a plan (often on paper) for "
# 						 "how a program will work. It involves big-picture "
# 						 "thinking and decision-making about a problem and "
# 						 "how different pieces of a program can work together "
# 						 "to solve it."),
# 		"examples" : [
# 			{"title" : "title-1",
# 			 "description" : "description-1"},
# 			{"title" : "title-2",
# 			 "description" : "description-2"}
# 		]
# 	},
# 	{"title" : "Debugging",
# 		"description" : ("Debugging is a systematic process of relentlessly "
# 						 "identifying the cause of a computer program that "
# 						 "doesn't work."),
# 		"examples" : [
# 			{"title" : "title-1",
# 			 "description" : "description-1"},
# 			{"title" : "title-2",
# 			 "description" : "description-2"}
# 		]
# 	},
# 	{"title" : "Technical Empathy",
# 		"description" : ("'Technological empathy' comes in many forms. For "
# 						 "example, computer empathy is the ability to "
# 						 "understand what a computer is, how it works, and "
# 						 "what it's good and bad at doing."),
# 		"examples" : [
# 			{"title" : "title-1",
# 			 "description" : "description-1"},
# 			{"title" : "title-2",
# 			 "description" : "description-2"}
# 		]
# 	}]
TOPICS = [
	{"title" : "CSS Positioning and Sizing",
	"description" : ("I really struggled with getting my HTML to "
					 "look right. I found these resources helpful."),
	"resources" : [
		{
		"title" : "Learn CSS Layout",
		"url" : "http://learnlayout.com/position.html",
		"description" : ("A good walk through of the `position` "
						 "property, including static, relative, fixed, "
						 "and absolute positioning.")
		},
		{
		"title" : "A Complete Guide to Flexbox",
		"url" : "https://css-tricks.com/snippets/css/a-guide-to-flexbox/",
		"description" : ("Flexbox is a, well, flexible box. It gives you "
						 "a way to have your HTML elements easily adjust "
						 "their size based on the size of the page.")
		},
		{
		"title" : "Intro to HTML and CSS",
		"url" : "https://www.udacity.com/course/ud304",
		"description" : ("The first lesson of this Udacity course is already "
						 "in the Nanodegree, but the rest of the course does "
						 "a good job of thoroughly explaining how to make web "
						 "pages look the way you want them to.")
		}
	]
	},
	{"title" : "Python Practice",
	"description" : ("Getting good at programming/Python requires a lot of practice. "
					 "These are some of my favorite sources of programming practice "
					 "problems."),
	"resources" : [
		{
		"title" : "Learn Python the Hard Way",
		"url" : "http://learnpythonthehardway.org/book/",
		"description" : ("This is a free online book by Zed Shaw. It's written "
						 "for novice programmers looking to learn Python. It's "
						 "organized by topic and has very good explanations and example "
						 "code throughout. Each section ends with helpful 'Study Drills.' "
						 "Highly recommended resource.")
		},
		{
		"title" : "Project Euler",
		"url" : "https://projecteuler.net/",
		"description" : ("This site provides a lot of highly mathematical "
						 "problems which can be solved with programming. It's a "
						 "good place for building your 'Procedural Thinking'.")
		},
		{
		"title" : "Coding Bat",
		"url" : "http://codingbat.com/python",
		"description" : ("Though the problems on this site all assume some "
						 "ability with Python functions, there is a good selection "
						 "of fairly easy problems (if you know how to use functions).")
		},
		{
		"title" : "More Resources from python.org",
		"url" : "https://wiki.python.org/moin/ProblemSets",
		"description" : ("The organization that manages the Python language also "
						 "maintains a list of practice resources as well. Some are "
						 "better than others.")
		}]},
	{"title" : 'Python "Web Frameworks"',
	"description" : ("A 'Web Framework' is a tool that facilitates the development "
		"of web applications. In Course 4, we used Google AppEngine to build our "
		"web app. The frameworks listed here can make it even easier to build large web "
		"applications by taking care of a lot of the necessary details for you."),
	"resources" : [
		{
		"title" : "Flask",
		"url" : "http://flask.pocoo.org/",
		"description" : ("The Django homepage says: \n\n"
			"Flask is a 'microframework'. It's simple to learn, easy to understand, and "
			"well-documented. It's great for small to medium sized projects.")
		},
		{
		"title" : "Django",
		"url" : "https://www.djangoproject.com/",
		"description" : ("The Django homepage says: \n\n"
			"Django is a high-level Python Web framework that encourages rapid "
			"development and clean, pragmatic design. Built by experienced developers, "
			"it takes care of much of the hassle of Web development, so you can focus on "
			"writing your app without needing to reinvent the wheel. It's free and open source.")
		},
		{
		"title" : "Flask vs. Django (Quora thread)",
		"url" : "http://www.quora.com/Should-I-learn-Flask-or-Django",
		"description" : ("Flask and Django are both very popular. This thread has "
			"some great discussion about the pros and cons of each. Summary: Django has more "
			"features, but Flask is easier to learn.")
		}
	]},
	{"title" : 'Other Udacity Nanodegrees',
	"description" : ("Once you've completed the Intro Programming Nanodegree, you'll "
		"be ready to take most (if not all) of Udacity's other Nanodegrees (which can "
		"actually prepare you for a job in programming)."),
	"resources" : [
		{
		"title" : "Front-End Web Developer Nanodegree",
		"url" : "https://www.udacity.com/course/nd001",
		"description" : ("In this Nanodegree you'll get a deeper understanding HTML and "
			"CSS and will develop ability with JavaScript, the third language of web development. "
			"You'll learn to build beautiful, responsive websites optimized for security and "
			"performance. You'll build six portfolio-worthy projects and learn how to do well "
			"in a programming job interview.")
		},
		{
		"title" : "iOS Developer Nanodegree",
		"url" : "https://www.udacity.com/course/nd003",
		"description" : ("iOS is the operating system used on iPhones and iPads. In this "
			"Nanodegree you learn the skills required to become an iOS "
			"Developer. Developing mobile apps can be a lot of fun (and often easier than web "
			"development in many ways). It can also be very lucrative: since iOS developers are in high "
		  "demand, there are many jobs available in the field. But it's also possible to make highly "
		  "successful apps on your own. In this Nanodegree program, you'll build five portfolio-worthy "
		  "iOS apps that demonstrate your expertise as an iOS Developer. You'll write all of these apps "
		  "in Swift, Apple's custom programming language developed specifically for building iOS and OS X apps.")
		},
		{
		"title" : "Full Stack Web Developer Nanodegree",
		"url" : "https://www.udacity.com/course/nd004",
		"description" : ("This Nanodegree program prepares you for a job as a Full Stack Web Developer. "
			"Participants in the program will learn to build complex server-side web applications that "
			"make use of powerful relational databases to persistently store data. You'll then learn how "
			"to secure and configure your very own Linux-based server to host your applications. Finally, "
			"you'll explore the challenges in horizontally scaling an application to support thousands of "
			"users with a cloud-based application hosting provider.")
		}
	]}]
SECTIONS = [
	{"title"     : "Andy's Course Notes",
	 "image_url" : "/images/computer_notes.jpg",
	 "href"      : "nanodegree_notes/",
	 "short_title":"Notes",
	 "id"        : "notes"
	},
	{"title"     : "Student Projects",
	 "image_url" : "/images/colored_papers.jpg",
	 "href"      : "student_submissions/",
	 "short_title":"Projects",
	 "id"        : "submissions"
	},
	{"title"     : "Additional Resources",
	 "image_url" : "/images/tools.jpg",
	 "href"      : "additional_resources/",
	 "short_title":"Resources",
	 "id"        : "resources"
	},
	# {"title"     : "Thinking Like a Programmer",
	#  "image_url" : "/images/blueprint.jpg",
	#  "href"      : "thinking_like_a_programmer/",
	#  "short_title":"Thinking",
	#  "id"        : "thinking"
	# },
	{"title"     : "Codepen Examples",
	 "image_url" : "/images/pen.jpg",
	 "href"      : "code_pen_examples/",
	 "short_title":"Codepens",
	 "id"        : "codepen"
	}]
def guestbook_key(guestbook_name=DEFAULT_GUESTBOOK_NAME):
	return ndb.Key('Guestbook', guestbook_name)

class Submission(ndb.Model):
  """A main model for representing an individual Guestbook entry."""
  # author = ndb.StructuredProperty(Author)
  link = ndb.StringProperty(indexed=False)
  description = ndb.StringProperty(indexed=False)
  date = ndb.DateTimeProperty(auto_now_add=True)
  image_url = ndb.StringProperty(indexed=False)
  name = ndb.StringProperty(indexed=False)

def code_examples_key(code_examples_name = DEFAULT_CODE_EXAMPLES_NAME):
	return ndb.Key('Code Examples', code_examples_name)

class CodeExample(ndb.Model):
	language = ndb.StringProperty(required=True, choices=["html", "css", "python", "other"])
	votes = ndb.IntegerProperty(default=0)
	date = ndb.DateTimeProperty(auto_now_add=True)
	title = ndb.StringProperty(required=True)
	description = ndb.StringProperty()
	url = ndb.StringProperty(required=True)
	def vote(self):
		self.votes = self.votes + 1

def code_pen_key(code_pen_name = DEFAULT_CODE_PEN_NAME):
	return ndb.Key('Code Pen Examples', code_pen_name)

class CodePenExample(ndb.Model):
	available_levels = ['beginner', 'intermediate', 'expert']
	votes = ndb.IntegerProperty(default=0)
	date = ndb.DateTimeProperty(auto_now_add=True)
	title = ndb.StringProperty(required=True)
	description = ndb.StringProperty()
	user_name = ndb.StringProperty(required=True)
	code_pen_id = ndb.StringProperty(required=True)
	level = ndb.StringProperty(required=True, choices=available_levels)






