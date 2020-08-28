<br>

<title>Colorizing the Prokudin-Gorskii Photo Collection</title>

<head>
  <meta charset="utf-8">
  <meta http-equiv="X-UA-Compatible" content="IE=edge">
  <!-- common.css -->
  <style>* {-webkit-tap-highlight-color: rgba(0,0,0,0);}html {-webkit-text-size-adjust: none;}body {font-family: -apple-system, Helvetica, Arial, sans-serif;margin: 0;padding: 20px;color: #333;word-wrap: break-word;}h1, h2, h3, h4, h5, h6 {line-height: 1.1;}img {max-width: 100% !important;height: auto;}blockquote {margin: 0;padding: 0 15px;color: #777;border-left: 4px solid #ddd;}hr {background-color: #ddd;border: 0;height: 1px;margin: 15px 0;}code {font-family: Menlo, Consolas, 'Ubuntu Mono', Monaco, 'source-code-pro', monospace;line-height: 1.4;margin: 0;padding: 0.2em 0;font-size: 90%;background-color: rgba(0,0,0,0.04);border-radius: 3px;}pre > code {margin: 0;padding: 0;font-size: 100%;word-break: normal;background: transparent;border: 0;}ol {list-style-type: decimal;}ol ol, ul ol {list-style-type: lower-latin;}ol ol ol, ul ol ol, ul ul ol, ol ul ol {list-style-type: lower-roman;}table {border-spacing: 0;border-collapse: collapse;margin-top: 0;margin-bottom: 16px;}table th {font-weight: bold;}table th, table td {padding: 6px 13px;border: 1px solid #ddd;}table tr {border-top: 1px solid #ccc;}table tr:nth-child(even) {background-color: #f8f8f8;}input[type="checkbox"] {cursor: default;margin-right: 0.5em;font-size: 13px;}.task-list-item {list-style-type: none;}.task-list-item+.task-list-item {margin-top: 3px;}.task-list-item input {float: left;margin: 0.3em 1em 0.25em -1.6em;vertical-align: middle;}#tag-field {margin: 8px 2px 10px;}#tag-field .tag {display: inline-block;background: #cadff3;border-radius: 4px;padding: 1px 8px;color: black;font-size: 12px;margin-right: 10px;line-height: 1.4;}</style>
  <!-- ace-static.css -->
  <style>.ace_static_highlight {white-space: pre-wrap;}.ace_static_highlight .ace_gutter {width: 2em;text-align: right;padding: 0 3px 0 0;margin-right: 3px;}.ace_static_highlight.ace_show_gutter > .ace_line {padding-left: 2.6em;}.ace_static_highlight .ace_line {position: relative;}.ace_static_highlight .ace_gutter-cell {-moz-user-select: -moz-none;-khtml-user-select: none;-webkit-user-select: none;user-select: none;top: 0;bottom: 0;left: 0;position: absolute;}.ace_static_highlight .ace_gutter-cell:before {content: counter(ace_line, decimal);counter-increment: ace_line;}.ace_static_highlight {counter-reset: ace_line;}</style>
  <style>.ace-chrome .ace_gutter {background: #ebebeb;color: #333;overflow : hidden;}.ace-chrome .ace_print-margin {width: 1px;background: #e8e8e8;}.ace-chrome {background-color: #FFFFFF;color: black;}.ace-chrome .ace_cursor {color: black;}.ace-chrome .ace_invisible {color: rgb(191, 191, 191);}.ace-chrome .ace_constant.ace_buildin {color: rgb(88, 72, 246);}.ace-chrome .ace_constant.ace_language {color: rgb(88, 92, 246);}.ace-chrome .ace_constant.ace_library {color: rgb(6, 150, 14);}.ace-chrome .ace_invalid {background-color: rgb(153, 0, 0);color: white;}.ace-chrome .ace_fold {}.ace-chrome .ace_support.ace_function {color: rgb(60, 76, 114);}.ace-chrome .ace_support.ace_constant {color: rgb(6, 150, 14);}.ace-chrome .ace_support.ace_type,.ace-chrome .ace_support.ace_class.ace-chrome .ace_support.ace_other {color: rgb(109, 121, 222);}.ace-chrome .ace_variable.ace_parameter {font-style:italic;color:#FD971F;}.ace-chrome .ace_keyword.ace_operator {color: rgb(104, 118, 135);}.ace-chrome .ace_comment {color: #236e24;}.ace-chrome .ace_comment.ace_doc {color: #236e24;}.ace-chrome .ace_comment.ace_doc.ace_tag {color: #236e24;}.ace-chrome .ace_constant.ace_numeric {color: rgb(0, 0, 205);}.ace-chrome .ace_variable {color: rgb(49, 132, 149);}.ace-chrome .ace_xml-pe {color: rgb(104, 104, 91);}.ace-chrome .ace_entity.ace_name.ace_function {color: #0000A2;}.ace-chrome .ace_heading {color: rgb(12, 7, 255);}.ace-chrome .ace_list {color:rgb(185, 6, 144);}.ace-chrome .ace_marker-layer .ace_selection {background: rgb(181, 213, 255);}.ace-chrome .ace_marker-layer .ace_step {background: rgb(252, 255, 0);}.ace-chrome .ace_marker-layer .ace_stack {background: rgb(164, 229, 101);}.ace-chrome .ace_marker-layer .ace_bracket {margin: -1px 0 0 -1px;border: 1px solid rgb(192, 192, 192);}.ace-chrome .ace_marker-layer .ace_active-line {background: rgba(0, 0, 0, 0.07);}.ace-chrome .ace_gutter-active-line {background-color : #dcdcdc;}.ace-chrome .ace_marker-layer .ace_selected-word {background: rgb(250, 250, 255);border: 1px solid rgb(200, 200, 250);}.ace-chrome .ace_storage,.ace-chrome .ace_keyword,.ace-chrome .ace_meta.ace_tag {color: rgb(147, 15, 128);}.ace-chrome .ace_string.ace_regex {color: rgb(255, 0, 0)}.ace-chrome .ace_string {color: #1A1AA6;}.ace-chrome .ace_entity.ace_other.ace_attribute-name {color: #994409;}.ace-chrome .ace_indent-guide {background: url("data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAEAAAACCAYAAACZgbYnAAAAE0lEQVQImWP4////f4bLly//BwAmVgd1/w11/gAAAABJRU5ErkJggg==") right repeat-y;}</style>
  <!-- export.css -->
  <style>
    body{margin:0 auto;max-width:1200px;line-height:1.4}
    #nav{margin:5px 0 10px;font-size:15px}
    #titlearea{border-bottom:1px solid #ccc;font-size:17px;padding:10px 0;}
    #contentarea{font-size:15px;margin:16px 0}
    .cell{outline:0;min-height:20px;margin:5px 0;padding:5px 0;}
    .code-cell{font-family:Menlo,Consolas,'Ubuntu Mono',Monaco,'source-code-pro',monospace;font-size:12px;}
    .latex-cell{white-space:pre-wrap;}
  </style>
  <!-- User CSS -->
  <style> .text-cell {font-size: 15px;}.code-cell {font-size: 12px;}.markdown-cell {font-size: 15px;}.latex-cell {font-size: 15px;}</style>
  <script type='text/x-mathjax-config'>MathJax.Hub.Config({tex2jax: {inlineMath: [['$','$']]}});</script>
  <script type='text/javascript' src='http://cdn.mathjax.org/mathjax/latest/MathJax.js?config=TeX-AMS-MML_HTMLorMML'></script>
</head>

# Images of the Russian Empire : Colorizing the Prokudin-Gorskii Photo Collection

## CS194-26 Project 1, Spring 2020

### By Sukrit Arora

#### sukrit.arora@berkeley.edu -- cs194-ahb

## Approach

The purpose of this assignment is to colorize the Prokudin-Gorskii photo collection. Each image contains information for each color channel (R, G, B); however, the data of each channel is not aligned. Thus, in order to generate a colored image, we need to align each color channel image so that the result is a cohesive colored image.

For smaller images, I exhaustively searched over a a window of [-15,15] for potential offsets in x and y and selected the values that minimized the SSD function (L2 Norm of flattened image difference).

For larger images, I used a multiscale pyramid to speed up computation. I first downsampled the image by $\log_2{\left(\max{\left(\text{image_dimensions}\right)}\right)}$ to get the smallest "base" image. I then calculate the offset on this image, upsample by a factor of 2, roll the resulting upsampled image by $2*offset$, and repeat this process until I get an image of the original dimensions.

For both kinds of images, I also crop the image so that we ignore the border when calculating offsets. For all images I shaved off 10% around the sides.

As you can see below, the results all around are fairly good. There are some images (melons, self_portrait) for which it doesn't perform too well, but for the other images (icon, wall_painting) the results are quite good.


## Small Image Results

#### monastery.jpg

Time Elapsed: 0.5207920074462891 for data/monastery.jpg

Green Offset: (-3, 2) for data/monastery.jpg

Red Offset: (3, 2) for data/monastery.jpg

![](out/monastery.jpg "Monastery")

#### tobolsk.jpg

Time Elapsed: 0.37480592727661133 for data/tobolsk.jpg

Green Offset: (3, 3) for data/tobolsk.jpg

Red Offset: (6, 3) for data/tobolsk.jpg

![](out/tobolsk.jpg "tobolsk")

#### cathedral.jpg

Time Elapsed: 0.4832148551940918 for data/cathedral.jpg

Green Offset: (5, 2) for data/cathedral.jpg

Red Offset: (12, 3) for data/cathedral.jpg

![](out/cathedral.jpg "cathedral")

## Large Image Results

#### workshop.tif

Time Elapsed: 8.361983060836792 for data/workshop.tif

Green Offset: (51, 0) for data/workshop.tif

Red Offset: (102, -11) for data/workshop.tif

![](out/workshop.jpg "Workshop")
 
#### emir.tif

Time Elapsed: 9.632888078689575 for data/emir.tif

Green Offset: (48, 23) for data/emir.tif

Red Offset: (100, 54) for data/emir.tif

![](out/emir.jpg "Emir") 
 
#### three_generations.tif

Time Elapsed: 9.591098070144653 for data/three_generations.tif

Green Offset: (52, 13) for data/three_generations.tif

Red Offset: (109, 11) for data/three_generations.tif

![](out/three_generations.jpg "three_generations")
 
#### melons.tif

Time Elapsed: 10.848026752471924 for data/melons.tif

Green Offset: (79, 9) for data/melons.tif

Red Offset: (155, 10) for data/melons.tif

![](out/melons.jpg "melons")
 
#### onion_church.tif

Time Elapsed: 10.901203155517578 for data/onion_church.tif

Green Offset: (49, 26) for data/onion_church.tif

Red Offset: (105, 35) for data/onion_church.tif

![](out/onion_church.jpg "onion_church")
 

#### train.tif

Time Elapsed: 12.388075828552246 for data/train.tif

Green Offset: (41, 5) for data/train.tif

Red Offset: (85, 31) for data/train.tif

![](out/train.jpg "train")
 
 
#### icon.tif

Time Elapsed: 11.453616857528687 for data/icon.tif

Green Offset: (39, 16) for data/icon.tif

Red Offset: (87, 22) for data/icon.tif

![](out/icon.jpg "icon")

 
#### village.tif

Time Elapsed: 11.199136018753052 for data/village.tif

Green Offset: (62, 11) for data/village.tif

Red Offset: (133, 22) for data/village.tif

![](out/village.jpg "village")
 
#### self_portrait.tif

Time Elapsed: 10.863592863082886 for data/self_portrait.tif

Green Offset: (76, 28) for data/self_portrait.tif

Red Offset: (155, 32) for data/self_portrait.tif

![](out/self_portrait.jpg "self_portrait")
 
#### harvesters.tif

Time Elapsed: 10.905174016952515 for data/harvesters.tif

Green Offset: (58, 16) for data/harvesters.tif

Red Offset: (120, 13) for data/harvesters.tif

![](out/harvesters.jpg "harvesters")

#### lady.tif

Time Elapsed: 10.896058082580566 for data/lady.tif

Green Offset: (49, 8) for data/lady.tif

Red Offset: (108, 11) for data/lady.tif

![](out/lady.jpg "lady")

## Extra Results from Library of Congress

#### [cheremukha.tif](https://www.loc.gov/pictures/collection/prok/item/2018679036/)

Time Elapsed: 10.82188606262207 for data/cheremukha.tif

Green Offset: (-29, -91) for data/cheremukha.tif

Red Offset: (22, -80) for data/cheremukha.tif

![](out/cheremukha.jpg "cheremukha")

#### [wall_painting.tif](https://www.loc.gov/pictures/collection/prok/item/2018678954/)

Time Elapsed: 10.01022219657898 for data/wall_painting.tif

Green Offset: (-20, 11) for data/wall_painting.tif

Red Offset: (-8, 26) for data/wall_painting.tif

![](out/wall_painting.jpg "Wall Painting")

 
#### [lodeinoe_pole.tif](https://www.loc.gov/pictures/collection/prok/item/2018678807/)

Time Elapsed: 11.175855159759521 for data/lodeinoe_pole.tif

Green Offset: (22, 20) for data/lodeinoe_pole.tif

Red Offset: (58, 28) for data/lodeinoe_pole.tif

![](out/lodeinoe_pole.jpg "lodeinoe_pole")