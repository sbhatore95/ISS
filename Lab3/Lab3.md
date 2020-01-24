# Lab3
## Sed

Sed is a stream editor that lets you edit a file without opening it in an editor like vim, emacs or
sublime. Editing takes place through the command line or from within a script.
How does sed work?
- Read : The file is read from an input stream (stdin, file, or pipe) and is stored in an
internal buffer
- Execute : All the sed commands are applied sequentially on this buffer
- Display: The changed content is sent to the output stream, and the buffer is emptied.
This process is repeated till the file ends. This happens on all lines unless otherwise specified.

Do note that all the sed commands are applied on the buffer, therefore the original file remains
unchanged.

Useful fact: Multiple sed commands can be written in a text file and can be given as an
argument to sed. Google how to do this !!

## Awk

Awk is a scripting language for text processing, and is much more powerful than sed. It allows
us to define variables, use arithmetic and string operators, use control flow, and generate
reports.
Here’s a good tutorial to learn its usage: [https://likegeeks.com/awk-command/]

## HTML and CSS
Here’s a good resource: [https://www.w3schools.com/html/]
An HTML file will contain the content of your website, and your CSS sheet — which stands for
Cascading Style Sheet — will style the content of your HTML file.

Related readings:

About the internet:
[https://developer.mozilla.org/en-US/docs/Learn/Common_questions/How_does_the_Internet_work]

WWW:
[https://developer.mozilla.org/en-US/docs/Learn/Getting_started_with_the_web/How_the_Web_works]

Cascading Style Sheets is the preferred way for setting the look and feel of a website.
The style sheets define the colour, size and position of text, etc, while the HTML files define the
content and how it is organised. Separating them allows you to change the colour scheme
without having to rewrite your entire web site.
The cascading means that a style applied to a parent element will also apply to all children
elements within the parent. For example, setting the colour of body text will mean all headings
and paragraphs within the body will also be the same colour.
There are 3 ways of doing this:
- Inline styles (set the style=”<>” attribute of a tag)
- Use the <style> tag within the header
- Create and link to an external css file

Look this up, and play around with styles to get comfortable with it.
[https://www.w3schools.com/css/css_intro.asp]

Activity:
See what's inside index.html in the files folder and open it in browser. Try editing it and adding new content.

Here’s a list of tags
[https://www.w3schools.com/tags/ref_byfunc.asp]

## JavaScript

JavaScript is a programming language that adds interactivity to your website (for example
games, responses when buttons are pressed or data is entered in forms, dynamic styling,
animation).

Basics
- Console.log
- Variables - declaration, initialization
- Datatypes - string, number, boolean, null, undefined
- Operators & arithmetic
- Comments
- Conditionals - if...else, switch
- Loops - for...in
- Strings and string functions - indexOf, replace, substring, toLowerCase/toUpperCase,
  trim, split, slice, concat, startsWith/endsWith, adding integer to string
- Array - creation ([], new Array()), assignment, non-integer indices, iterating using
  ForEach, push/pop, shift, concat, sort, slice, splice, join
- == vs ===
- Functions (basic)

Links for Practice:
1. [https://www.codecademy.com/learn/introduction-to-javascript]

References:
1. https://developers.google.com/apps-script/guides/html/best-practices
2. https://google.github.io/styleguide/jsguide.html

## DOM
- DOM tree
- Window and document objects
- getElementbyId, getElementbyClassName, getElementbyTagName, createElement,
- appendChild
- Manipulating HTML and CSS - element.innerHTML, .style, .setAttribute, .getAttribute
- element.innerText vs element.innerHTML
- Events - click, hover, change, element.<event> vs element.addEventListener
