/*
 * This file was automatically generated.
 * DO NOT MODIFY BY HAND.
 * Run `yarn special-lint-fix` to update
 */
"use strict";function r(t,{instancePath:e="",parentData:o,parentDataProperty:a,rootData:n=t}={}){if(!t||"object"!=typeof t||Array.isArray(t))return r.errors=[{params:{type:"object"}}],!1;{const e=0;for(const e in t)if("import"!==e&&"namedExports"!==e&&"url"!==e)return r.errors=[{params:{additionalProperty:e}}],!1;if(0===e){if(void 0!==t.import){const e=0;if("boolean"!=typeof t.import)return r.errors=[{params:{type:"boolean"}}],!1;var s=0===e}else s=!0;if(s){if(void 0!==t.namedExports){const e=0;if("boolean"!=typeof t.namedExports)return r.errors=[{params:{type:"boolean"}}],!1;s=0===e}else s=!0;if(s)if(void 0!==t.url){const e=0;if("boolean"!=typeof t.url)return r.errors=[{params:{type:"boolean"}}],!1;s=0===e}else s=!0}}}return r.errors=null,!0}function t(e,{instancePath:o="",parentData:a,parentDataProperty:n,rootData:s=e}={}){let p=null,i=0;return r(e,{instancePath:o,parentData:a,parentDataProperty:n,rootData:s})||(p=null===p?r.errors:p.concat(r.errors),i=p.length),t.errors=p,0===i}module.exports=t,module.exports.default=t;