#!c:\Python\python.exe
# Fig. 35.18: fig35_18.py
# Program to read information sent to the server from the
# form in the form.html document.

import cgi
import re

# the regular expression for matching most US phone numbers.
telephoneExpression = \
   re.compile( r'^\(\d{3}\)\d{3}-\d{4}$' )

def printContent():
   print "Content-type: text/html"
   print
   print """
<html xmlns = "http://www.w3.org/1999/xhtml" xml:lang="en"
   lang="en">
   <head><title>Registration results</title>
   <link href="/style.css" rel="stylesheet" type="text/css" />
   </head>
      <body><div id="header-wrap">
    <div id="header">
      <div class="wrap">
        <div class="branding">
          <h1 id="blog-title" class="blogtitle"><a href="/" title="UPEI APP 11">UPEI App
          11</a></h1>
        </div><!-- .branding -->
      </div><!-- .wrap -->
    </div><!--  #header -->
  </div>"""
   
def printReply():
   print """
   <div id="wrapper">
    <div class="clear"></div>

    <div id="container">
      <div id="content">
        <div id="post-0">
          <div class="hentry">
            <h2 class="entry-title">Thanks!</h2>

            <div class="entry-content">
      Hi <span style = "color: blue; font-weight: bold">
      %(firstName)s</span>.
      Thank you for completing the survey.<br />
      You have been added to the <span style = "color: blue;
      font-weight: bold">%(book)s </span> mailing list.<br /><br />

      <span style = "font-weight: bold">
      The following information has been saved in our database:
      </span><br />

      <table style = "border: 0; border-width: 0;
         border-spacing: 10">
      <tr><td style = "background-color: yellow">Name </td>
          <td style = "background-color: yellow">Email</td>
          <td style = "background-color: yellow">Phone</td>
          <td style = "background-color: yellow">OS</td></tr>

      <tr><td>%(firstName)s %(lastName)s</td><td>%(email)s</td>
          <td>%(phone)s</td><td>%(os)s</td></tr>
      </table>

      <br /><br /><br />

      <div style = "text-align: center; font-size: 8pt">
      This is only a sample form. 
      You have not been added to a mailing list.
      </div></center></div>
          </div>
        </div>
      </div>
    </div>
  </div>

  <div id="footer"></div></body></html>
      """ % personInfo

def printPhoneError():

   print """<span style = "color: red; font-size 15pt">
      INVALID PHONE NUMBER</span><br />
      A valid phone number must be in the form
      <span style = "font-weight: bold">(555)555-5555</span>
      <span style = "color: blue"> Click the Back button, 
      enter a valid phone number and resubmit.</span><br /><br />
      Thank You.</body></html>"""
      
def printFormError():

   print """<span style = "color: red; font-size 15pt">
      FORM ERROR</span><br />
      You have not filled in all fields.
      <span style = "color: blue"> Click the Back button, 
      fill out the form and resubmit.</span><br /><br />
      Thank You.</body></html>"""
     
printContent()

form = cgi.FieldStorage()

try:
   personInfo = { 'firstName' : form[ "firstname" ].value,
                  'lastName' : form[ "lastname" ].value,
                  'email' : form[ "email" ].value,
                  'phone' : form[ "phone" ].value,
                  'book' : form[ "book" ].value,
                  'os' : form[ "os" ].value }
except KeyError:
   printFormError()
      
if telephoneExpression.match( personInfo[ 'phone' ] ):
   printReply()
else:
   printPhoneError()  


########################################################################## 
# (C) Copyright 1992-2004 by Deitel & Associates, Inc. and               #
# Pearson Education, Inc. All Rights Reserved.                           #
#                                                                        #
# DISCLAIMER: The authors and publisher of this book have used their     #
# best efforts in preparing the book. These efforts include the          #
# development, research, and testing of the theories and programs        #
# to determine their effectiveness. The authors and publisher make       #
# no warranty of any kind, expressed or implied, with regard to these    #
# programs or to the documentation contained in these books. The authors #
# and publisher shall not be liable in any event for incidental or       #
# consequential damages in connection with, or arising out of, the       #
# furnishing, performance, or use of these programs.                     #
##########################################################################
