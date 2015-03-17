# TODO : Add comments throughout
# TODO : Minimize everything! LESS CODE, more abstraction
# TODO : Change duplicate names! No lines of code that say examples=examples!
# TODO : Change for loops to not ALL be `for element in elements` No Pluralization magic!

import os
import webapp2
import jinja2
from urlparse import urlparse

from content import COURSES, TOPICS, SECTIONS, guestbook_key, Submission, code_examples_key, CodeExample, code_pen_key, CodePenExample, DEFAULT_GUESTBOOK_NAME, DEFAULT_CODE_EXAMPLES_NAME, DEFAULT_CODE_PEN_NAME
import urllib


template_dir = os.path.join(os.path.dirname(__file__), 'html_templates')
jinja_env = jinja2.Environment(
	loader = jinja2.FileSystemLoader(template_dir),
	extensions=['jinja2.ext.autoescape'],
	autoescape=True)


class Handler(webapp2.RequestHandler):
	def write(self, *a, **kw):
		self.response.out.write(*a, **kw)

	def render_str(self, template, **params):
		t = jinja_env.get_template(template)
		return t.render(params)

	def render(self, template, **kw):
		self.write(self.render_str(template, courses=COURSES, sections=SECTIONS, **kw))

class MainPage(Handler):
	def get(self):
		self.render("main_page.html", page_name="home")

class NanodegreeHandler(Handler):
	def get(self):
		self.render('nanodegree_notes.html', page_name="notes")

class CourseHandler(Handler):
	def get(self, course_number):
		self.render("course.html", course_number=int(course_number), course=COURSES[int(course_number)-1], page_name="notes")

class LessonHandler(Handler):
	def get(self, course_number, lesson_number):
		self.render("lesson.html", lesson_number=int(lesson_number), lesson=COURSES[int(course_number)-1]['lessons'][int(lesson_number)-1], page_name="notes")

class ThinkingHandler(Handler):
	def get(self):
		self.render('thinking_like_a_programmer.html', ways_of_thinking=THINKING, page_name="thinking")

class ResourcesHandler(Handler):
	def get(self):
		self.render('additional_resources.html', topics=TOPICS, page_name="resources")

class SubmissionListHandler(Handler):
	def get(self):
		guestbook_name = self.request.get('guestbook_name', DEFAULT_GUESTBOOK_NAME)
		submissions_query = Submission.query(
			ancestor=guestbook_key(guestbook_name)).order(-Submission.date)
		submissions = submissions_query.fetch(10)
		self.render('guestbook.html', submissions=submissions, page_name="submissions")

class CodePenVoteHandler(Handler):
	def post(self):
		code_pen_name = self.request.get('code_pen_name', DEFAULT_CODE_PEN_NAME)
		code_pen_id = self.request.get('vote_up')
		code_pen_query = CodePenExample.query(
			CodePenExample.code_pen_id == code_pen_id,
			ancestor=code_pen_key(code_pen_name))
		code_pens = code_pen_query.fetch()
		code_pen=code_pens[0]
		code_pen.votes = code_pen.votes + 1
		print
		print code_pen
		print
		print "VOTES = %i" % code_pen.votes
		code_pen.put()
		self.redirect('/code_pen_examples/')

class SubmissionHandler(Handler):
	def get(self):
		self.render('add_submission.html', page_name="submissions" )
	def post(self):
		guestbook_name = self.request.get('guestbook_name', DEFAULT_GUESTBOOK_NAME)
		submission = Submission(parent=guestbook_key(guestbook_name))
		submission.name = self.request.get('name')
		submission.link = self.request.get('link')
		submission.description = self.request.get('description')
		submission.image_url = self.request.get('image_url')
		submission.put()
		# query_params = {'guestbook_name' : guestbook_name}
		self.redirect('/student_submissions/') # + urllib.urlencode(query_params))

class CodePenExampleListHandler(Handler):
	def get(self, levels=CodePenExample.available_levels, available_levels=CodePenExample.available_levels, error=False):
		code_pen_name = self.request.get('code_pen_name', DEFAULT_CODE_PEN_NAME)
		examples_query = CodePenExample.query(
			# CodePenExample.level in levels,
			ancestor=code_pen_key(code_pen_name)).order(-CodePenExample.votes)
		examples = examples_query.fetch(10)
		self.render('code_pen_examples.html', examples=examples, levels=levels, page_name="codepen", available_levels=available_levels)
	def post(self):
		code_pen_name = self.request.get('code_pen_name', DEFAULT_CODE_PEN_NAME)
		pen = CodePenExample(parent=code_pen_key(code_pen_name))

		pen.level = self.request.get('level')
		pen.title = self.request.get('title')
		pen.description= self.request.get('description')
		input_url = self.request.get('url')
		url_info = self.get_user_name_and_pen_id(input_url)
		if url_info['valid_url']:
			pen.user_name = url_info['user_name']
			pen.code_pen_id = url_info['code_pen_id']
			pen.put()
			self.redirect('/code_pen_examples/')
		else:
			self.get(error=url_info['error_message'])
	def get_user_name_and_pen_id(self, input_url):
	    try:
	        url_pieces = urlparse(input_url)

	        scheme = url_pieces.scheme
	        if scheme != 'http':
	            return {'valid_url': False,
	                    'error_message' : 'Your link should begin with http://'}

	        host = url_pieces.netloc
	        if host != 'codepen.io':
	            return {'valid_url': False,
	                    'error_message': 'The link you submitted is not to codepen.io'}

	        path = url_pieces.path
	        path_segments = path.split('/')
	        if len(path_segments) != 4:
	            return {'valid_url' : False,
	                    'error_message' : 'That URL does not go to a pen in codepen.'}

	        user_name   = path_segments[1]
	        code_pen_id = path_segments[3]
	        return {'user_name'   : user_name,
	                'code_pen_id' : code_pen_id,
	                'valid_url'   : True}
	    except:
	        return {'valid_url'     : False,
	                'error_message' : "That isn't a valid codepen URL. Make sure to copy and paste your URL from codepen exactly."}

		# self.redirect('/example_code/')

# class CodePenExampleHandler(Handler):
# 	def get(self):
# 		self.render('add_example.html', page_name="example code")
# 	def post(self, language):
# 		code_pen_name = self.request.get('code_pen_name', DEFAULT_CODE_PEN_NAME)
# 		pen = CodeExample(parent=code_pen_key(code_pen_name))
# 		pen.language = language.lower()
# 		pen.title = self.request.get('title')
# 		pen.description= self.request.get('description')
# 		pen.url = self.request.get('url')
# 		pen.put()
# 		self.redirect('/example_code/%s/' % language)





















