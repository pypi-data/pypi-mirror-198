"use strict";/*!-----------------------------------------------------------------------------
 * Copyright (c) Microsoft Corporation. All rights reserved.
 * Version: 0.35.0(71ac097e6155a405f6be52b0b368a04508c31e31)
 * Released under the MIT license
 * https://github.com/microsoft/monaco-editor/blob/main/LICENSE.txt
 *-----------------------------------------------------------------------------*/
define("vs/basic-languages/less/less", ["require","require"],(require)=>{
var moduleExports=(()=>{var r=Object.defineProperty;var s=Object.getOwnPropertyDescriptor;var a=Object.getOwnPropertyNames;var l=Object.prototype.hasOwnProperty;var d=(t,e)=>{for(var i in e)r(t,i,{get:e[i],enumerable:!0})},u=(t,e,i,o)=>{if(e&&typeof e=="object"||typeof e=="function")for(let n of a(e))!l.call(t,n)&&n!==i&&r(t,n,{get:()=>e[n],enumerable:!(o=s(e,n))||o.enumerable});return t};var c=t=>u(r({},"__esModule",{value:!0}),t);var p={};d(p,{conf:()=>m,language:()=>g});var m={wordPattern:/(#?-?\d*\.\d\w*%?)|([@#!.:]?[\w-?]+%?)|[@#!.]/g,comments:{blockComment:["/*","*/"],lineComment:"//"},brackets:[["{","}"],["[","]"],["(",")"]],autoClosingPairs:[{open:"{",close:"}",notIn:["string","comment"]},{open:"[",close:"]",notIn:["string","comment"]},{open:"(",close:")",notIn:["string","comment"]},{open:'"',close:'"',notIn:["string","comment"]},{open:"'",close:"'",notIn:["string","comment"]}],surroundingPairs:[{open:"{",close:"}"},{open:"[",close:"]"},{open:"(",close:")"},{open:'"',close:'"'},{open:"'",close:"'"}],folding:{markers:{start:new RegExp("^\\s*\\/\\*\\s*#region\\b\\s*(.*?)\\s*\\*\\/"),end:new RegExp("^\\s*\\/\\*\\s*#endregion\\b.*\\*\\/")}}},g={defaultToken:"",tokenPostfix:".less",identifier:"-?-?([a-zA-Z]|(\\\\(([0-9a-fA-F]{1,6}\\s?)|[^[0-9a-fA-F])))([\\w\\-]|(\\\\(([0-9a-fA-F]{1,6}\\s?)|[^[0-9a-fA-F])))*",identifierPlus:"-?-?([a-zA-Z:.]|(\\\\(([0-9a-fA-F]{1,6}\\s?)|[^[0-9a-fA-F])))([\\w\\-:.]|(\\\\(([0-9a-fA-F]{1,6}\\s?)|[^[0-9a-fA-F])))*",brackets:[{open:"{",close:"}",token:"delimiter.curly"},{open:"[",close:"]",token:"delimiter.bracket"},{open:"(",close:")",token:"delimiter.parenthesis"},{open:"<",close:">",token:"delimiter.angle"}],tokenizer:{root:[{include:"@nestedJSBegin"},["[ \\t\\r\\n]+",""],{include:"@comments"},{include:"@keyword"},{include:"@strings"},{include:"@numbers"},["[*_]?[a-zA-Z\\-\\s]+(?=:.*(;|(\\\\$)))","attribute.name","@attribute"],["url(\\-prefix)?\\(",{token:"tag",next:"@urldeclaration"}],["[{}()\\[\\]]","@brackets"],["[,:;]","delimiter"],["#@identifierPlus","tag.id"],["&","tag"],["\\.@identifierPlus(?=\\()","tag.class","@attribute"],["\\.@identifierPlus","tag.class"],["@identifierPlus","tag"],{include:"@operators"},["@(@identifier(?=[:,\\)]))","variable","@attribute"],["@(@identifier)","variable"],["@","key","@atRules"]],nestedJSBegin:[["``","delimiter.backtick"],["`",{token:"delimiter.backtick",next:"@nestedJSEnd",nextEmbedded:"text/javascript"}]],nestedJSEnd:[["`",{token:"delimiter.backtick",next:"@pop",nextEmbedded:"@pop"}]],operators:[["[<>=\\+\\-\\*\\/\\^\\|\\~]","operator"]],keyword:[["(@[\\s]*import|![\\s]*important|true|false|when|iscolor|isnumber|isstring|iskeyword|isurl|ispixel|ispercentage|isem|hue|saturation|lightness|alpha|lighten|darken|saturate|desaturate|fadein|fadeout|fade|spin|mix|round|ceil|floor|percentage)\\b","keyword"]],urldeclaration:[{include:"@strings"},[`[^)\r
]+`,"string"],["\\)",{token:"tag",next:"@pop"}]],attribute:[{include:"@nestedJSBegin"},{include:"@comments"},{include:"@strings"},{include:"@numbers"},{include:"@keyword"},["[a-zA-Z\\-]+(?=\\()","attribute.value","@attribute"],[">","operator","@pop"],["@identifier","attribute.value"],{include:"@operators"},["@(@identifier)","variable"],["[)\\}]","@brackets","@pop"],["[{}()\\[\\]>]","@brackets"],["[;]","delimiter","@pop"],["[,=:]","delimiter"],["\\s",""],[".","attribute.value"]],comments:[["\\/\\*","comment","@comment"],["\\/\\/+.*","comment"]],comment:[["\\*\\/","comment","@pop"],[".","comment"]],numbers:[["(\\d*\\.)?\\d+([eE][\\-+]?\\d+)?",{token:"attribute.value.number",next:"@units"}],["#[0-9a-fA-F_]+(?!\\w)","attribute.value.hex"]],units:[["(em|ex|ch|rem|fr|vmin|vmax|vw|vh|vm|cm|mm|in|px|pt|pc|deg|grad|rad|turn|s|ms|Hz|kHz|%)?","attribute.value.unit","@pop"]],strings:[['~?"',{token:"string.delimiter",next:"@stringsEndDoubleQuote"}],["~?'",{token:"string.delimiter",next:"@stringsEndQuote"}]],stringsEndDoubleQuote:[['\\\\"',"string"],['"',{token:"string.delimiter",next:"@popall"}],[".","string"]],stringsEndQuote:[["\\\\'","string"],["'",{token:"string.delimiter",next:"@popall"}],[".","string"]],atRules:[{include:"@comments"},{include:"@strings"},["[()]","delimiter"],["[\\{;]","delimiter","@pop"],[".","key"]]}};return c(p);})();
return moduleExports;
});
