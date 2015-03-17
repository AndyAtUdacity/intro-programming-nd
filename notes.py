import webapp2
import cgi
from handlers import *

application = webapp2.WSGIApplication([
	('/code_pen_examples/', CodePenExampleListHandler),
	('/code_pen_examples/vote', CodePenVoteHandler),
	('/additional_resources/', ResourcesHandler),
	('/nanodegree_notes/', NanodegreeHandler),
	('/thinking_like_a_programmer/', ThinkingHandler),
  (r'/nanodegree_notes/course/(\d+)/', CourseHandler),
  (r'/nanodegree_notes/course/(\d+)/lesson/(\d+)/', LessonHandler),
  ('/student_submissions/add', SubmissionHandler),
  ('/student_submissions/', SubmissionListHandler),
  ('/*', MainPage)
], debug=True)



