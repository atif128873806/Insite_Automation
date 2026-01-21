/** © 2025, Insite Life Ltd. All rights reserved. **/
function e(e){this.message=e;}e.prototype=new Error,e.prototype.name="InvalidCharacterError";var r="undefined"!=typeof window&&window.atob&&window.atob.bind(window)||function(r){var t=String(r).replace(/=+$/,"");if(t.length%4==1)throw new e("'atob' failed: The string to be decoded is not correctly encoded.");for(var n,o,a=0,i=0,c="";o=t.charAt(i++);~o&&(n=a%4?64*n+o:o,a++%4)?c+=String.fromCharCode(255&n>>(-2*a&6)):0)o="ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/=".indexOf(o);return c};function t(e){var t=e.replace(/-/g,"+").replace(/_/g,"/");switch(t.length%4){case 0:break;case 2:t+="==";break;case 3:t+="=";break;default:throw "Illegal base64url string!"}try{return function(e){return decodeURIComponent(r(e).replace(/(.)/g,function(e,r){var t=r.charCodeAt(0).toString(16).toUpperCase();return t.length<2&&(t="0"+t),"%"+t}))}(t)}catch(e){return r(t)}}function n(e){this.message=e;}function o(e,r){if("string"!=typeof e)throw new n("Invalid token specified");var o=!0===(r=r||{}).header?0:1;try{return JSON.parse(t(e.split(".")[o]))}catch(e){throw new n("Invalid token specified: "+e.message)}}n.prototype=new Error,n.prototype.name="InvalidTokenError";var commonjsGlobal="undefined"!=typeof globalThis?globalThis:"undefined"!=typeof window?window:"undefined"!=typeof global?global:"undefined"!=typeof self?self:{};function getDefaultExportFromCjs(x){return x&&x.__esModule&&Object.prototype.hasOwnProperty.call(x,"default")?x.default:x}var browserPolyfill={exports:{}};(function(module){if(!globalThis.chrome?.runtime?.id)throw new Error("This script should only be loaded in a browser extension.");if(void 0===globalThis.browser||Object.getPrototypeOf(globalThis.browser)!==Object.prototype){const CHROME_SEND_MESSAGE_CALLBACK_NO_RESPONSE_MESSAGE="The message port closed before a response was received.",wrapAPIs=extensionAPIs=>{
// NOTE: apiMetadata is associated to the content of the api-metadata.json file
// at build time by replacing the following "include" with the content of the
// JSON file.
const apiMetadata={alarms:{clear:{minArgs:0,maxArgs:1},clearAll:{minArgs:0,maxArgs:0},get:{minArgs:0,maxArgs:1},getAll:{minArgs:0,maxArgs:0}},bookmarks:{create:{minArgs:1,maxArgs:1},get:{minArgs:1,maxArgs:1},getChildren:{minArgs:1,maxArgs:1},getRecent:{minArgs:1,maxArgs:1},getSubTree:{minArgs:1,maxArgs:1},getTree:{minArgs:0,maxArgs:0},move:{minArgs:2,maxArgs:2},remove:{minArgs:1,maxArgs:1},removeTree:{minArgs:1,maxArgs:1},search:{minArgs:1,maxArgs:1},update:{minArgs:2,maxArgs:2}},browserAction:{disable:{minArgs:0,maxArgs:1,fallbackToNoCallback:!0},enable:{minArgs:0,maxArgs:1,fallbackToNoCallback:!0},getBadgeBackgroundColor:{minArgs:1,maxArgs:1},getBadgeText:{minArgs:1,maxArgs:1},getPopup:{minArgs:1,maxArgs:1},getTitle:{minArgs:1,maxArgs:1},openPopup:{minArgs:0,maxArgs:0},setBadgeBackgroundColor:{minArgs:1,maxArgs:1,fallbackToNoCallback:!0},setBadgeText:{minArgs:1,maxArgs:1,fallbackToNoCallback:!0},setIcon:{minArgs:1,maxArgs:1},setPopup:{minArgs:1,maxArgs:1,fallbackToNoCallback:!0},setTitle:{minArgs:1,maxArgs:1,fallbackToNoCallback:!0}},browsingData:{remove:{minArgs:2,maxArgs:2},removeCache:{minArgs:1,maxArgs:1},removeCookies:{minArgs:1,maxArgs:1},removeDownloads:{minArgs:1,maxArgs:1},removeFormData:{minArgs:1,maxArgs:1},removeHistory:{minArgs:1,maxArgs:1},removeLocalStorage:{minArgs:1,maxArgs:1},removePasswords:{minArgs:1,maxArgs:1},removePluginData:{minArgs:1,maxArgs:1},settings:{minArgs:0,maxArgs:0}},commands:{getAll:{minArgs:0,maxArgs:0}},contextMenus:{remove:{minArgs:1,maxArgs:1},removeAll:{minArgs:0,maxArgs:0},update:{minArgs:2,maxArgs:2}},cookies:{get:{minArgs:1,maxArgs:1},getAll:{minArgs:1,maxArgs:1},getAllCookieStores:{minArgs:0,maxArgs:0},remove:{minArgs:1,maxArgs:1},set:{minArgs:1,maxArgs:1}},devtools:{inspectedWindow:{eval:{minArgs:1,maxArgs:2,singleCallbackArg:!1}},panels:{create:{minArgs:3,maxArgs:3,singleCallbackArg:!0},elements:{createSidebarPane:{minArgs:1,maxArgs:1}}}},downloads:{cancel:{minArgs:1,maxArgs:1},download:{minArgs:1,maxArgs:1},erase:{minArgs:1,maxArgs:1},getFileIcon:{minArgs:1,maxArgs:2},open:{minArgs:1,maxArgs:1,fallbackToNoCallback:!0},pause:{minArgs:1,maxArgs:1},removeFile:{minArgs:1,maxArgs:1},resume:{minArgs:1,maxArgs:1},search:{minArgs:1,maxArgs:1},show:{minArgs:1,maxArgs:1,fallbackToNoCallback:!0}},extension:{isAllowedFileSchemeAccess:{minArgs:0,maxArgs:0},isAllowedIncognitoAccess:{minArgs:0,maxArgs:0}},history:{addUrl:{minArgs:1,maxArgs:1},deleteAll:{minArgs:0,maxArgs:0},deleteRange:{minArgs:1,maxArgs:1},deleteUrl:{minArgs:1,maxArgs:1},getVisits:{minArgs:1,maxArgs:1},search:{minArgs:1,maxArgs:1}},i18n:{detectLanguage:{minArgs:1,maxArgs:1},getAcceptLanguages:{minArgs:0,maxArgs:0}},identity:{launchWebAuthFlow:{minArgs:1,maxArgs:1}},idle:{queryState:{minArgs:1,maxArgs:1}},management:{get:{minArgs:1,maxArgs:1},getAll:{minArgs:0,maxArgs:0},getSelf:{minArgs:0,maxArgs:0},setEnabled:{minArgs:2,maxArgs:2},uninstallSelf:{minArgs:0,maxArgs:1}},notifications:{clear:{minArgs:1,maxArgs:1},create:{minArgs:1,maxArgs:2},getAll:{minArgs:0,maxArgs:0},getPermissionLevel:{minArgs:0,maxArgs:0},update:{minArgs:2,maxArgs:2}},pageAction:{getPopup:{minArgs:1,maxArgs:1},getTitle:{minArgs:1,maxArgs:1},hide:{minArgs:1,maxArgs:1,fallbackToNoCallback:!0},setIcon:{minArgs:1,maxArgs:1},setPopup:{minArgs:1,maxArgs:1,fallbackToNoCallback:!0},setTitle:{minArgs:1,maxArgs:1,fallbackToNoCallback:!0},show:{minArgs:1,maxArgs:1,fallbackToNoCallback:!0}},permissions:{contains:{minArgs:1,maxArgs:1},getAll:{minArgs:0,maxArgs:0},remove:{minArgs:1,maxArgs:1},request:{minArgs:1,maxArgs:1}},runtime:{getBackgroundPage:{minArgs:0,maxArgs:0},getPlatformInfo:{minArgs:0,maxArgs:0},openOptionsPage:{minArgs:0,maxArgs:0},requestUpdateCheck:{minArgs:0,maxArgs:0},sendMessage:{minArgs:1,maxArgs:3},sendNativeMessage:{minArgs:2,maxArgs:2},setUninstallURL:{minArgs:1,maxArgs:1}},sessions:{getDevices:{minArgs:0,maxArgs:1},getRecentlyClosed:{minArgs:0,maxArgs:1},restore:{minArgs:0,maxArgs:1}},storage:{local:{clear:{minArgs:0,maxArgs:0},get:{minArgs:0,maxArgs:1},getBytesInUse:{minArgs:0,maxArgs:1},remove:{minArgs:1,maxArgs:1},set:{minArgs:1,maxArgs:1}},managed:{get:{minArgs:0,maxArgs:1},getBytesInUse:{minArgs:0,maxArgs:1}},sync:{clear:{minArgs:0,maxArgs:0},get:{minArgs:0,maxArgs:1},getBytesInUse:{minArgs:0,maxArgs:1},remove:{minArgs:1,maxArgs:1},set:{minArgs:1,maxArgs:1}}},tabs:{captureVisibleTab:{minArgs:0,maxArgs:2},create:{minArgs:1,maxArgs:1},detectLanguage:{minArgs:0,maxArgs:1},discard:{minArgs:0,maxArgs:1},duplicate:{minArgs:1,maxArgs:1},executeScript:{minArgs:1,maxArgs:2},get:{minArgs:1,maxArgs:1},getCurrent:{minArgs:0,maxArgs:0},getZoom:{minArgs:0,maxArgs:1},getZoomSettings:{minArgs:0,maxArgs:1},goBack:{minArgs:0,maxArgs:1},goForward:{minArgs:0,maxArgs:1},highlight:{minArgs:1,maxArgs:1},insertCSS:{minArgs:1,maxArgs:2},move:{minArgs:2,maxArgs:2},query:{minArgs:1,maxArgs:1},reload:{minArgs:0,maxArgs:2},remove:{minArgs:1,maxArgs:1},removeCSS:{minArgs:1,maxArgs:2},sendMessage:{minArgs:2,maxArgs:3},setZoom:{minArgs:1,maxArgs:2},setZoomSettings:{minArgs:1,maxArgs:2},update:{minArgs:1,maxArgs:2}},topSites:{get:{minArgs:0,maxArgs:0}},webNavigation:{getAllFrames:{minArgs:1,maxArgs:1},getFrame:{minArgs:1,maxArgs:1}},webRequest:{handlerBehaviorChanged:{minArgs:0,maxArgs:0}},windows:{create:{minArgs:0,maxArgs:1},get:{minArgs:1,maxArgs:2},getAll:{minArgs:0,maxArgs:1},getCurrent:{minArgs:0,maxArgs:1},getLastFocused:{minArgs:0,maxArgs:1},remove:{minArgs:1,maxArgs:1},update:{minArgs:2,maxArgs:2}}};if(0===Object.keys(apiMetadata).length)throw new Error("api-metadata.json has not been included in browser-polyfill");
/**
	       * A WeakMap subclass which creates and stores a value for any key which does
	       * not exist when accessed, but behaves exactly as an ordinary WeakMap
	       * otherwise.
	       *
	       * @param {function} createItem
	       *        A function which will be called in order to create the value for any
	       *        key which does not exist, the first time it is accessed. The
	       *        function receives, as its only argument, the key being created.
	       */class DefaultWeakMap extends WeakMap{constructor(createItem,items=void 0){super(items),this.createItem=createItem;}get(key){return this.has(key)||this.set(key,this.createItem(key)),super.get(key)}}
/**
	       * Returns true if the given object is an object with a `then` method, and can
	       * therefore be assumed to behave as a Promise.
	       *
	       * @param {*} value The value to test.
	       * @returns {boolean} True if the value is thenable.
	       */const isThenable=value=>value&&"object"==typeof value&&"function"==typeof value.then,makeCallback=(promise,metadata)=>(...callbackArgs)=>{extensionAPIs.runtime.lastError?promise.reject(new Error(extensionAPIs.runtime.lastError.message)):metadata.singleCallbackArg||callbackArgs.length<=1&&!1!==metadata.singleCallbackArg?promise.resolve(callbackArgs[0]):promise.resolve(callbackArgs);},pluralizeArguments=numArgs=>1==numArgs?"argument":"arguments",wrapAsyncFunction=(name,metadata)=>function(target,...args){if(args.length<metadata.minArgs)throw new Error(`Expected at least ${metadata.minArgs} ${pluralizeArguments(metadata.minArgs)} for ${name}(), got ${args.length}`);if(args.length>metadata.maxArgs)throw new Error(`Expected at most ${metadata.maxArgs} ${pluralizeArguments(metadata.maxArgs)} for ${name}(), got ${args.length}`);return new Promise((resolve,reject)=>{if(metadata.fallbackToNoCallback)
// This API method has currently no callback on Chrome, but it return a promise on Firefox,
// and so the polyfill will try to call it with a callback first, and it will fallback
// to not passing the callback if the first call fails.
try{target[name](...args,makeCallback({resolve,reject},metadata));}catch(cbError){console.warn(`${name} API method doesn't seem to support the callback parameter, falling back to call it without a callback: `,cbError),target[name](...args),// Update the API method metadata, so that the next API calls will not try to
// use the unsupported callback anymore.
metadata.fallbackToNoCallback=!1,metadata.noCallback=!0,resolve();}else metadata.noCallback?(target[name](...args),resolve()):target[name](...args,makeCallback({resolve,reject},metadata));})},wrapMethod=(target,method,wrapper)=>new Proxy(method,{apply:(targetMethod,thisObj,args)=>wrapper.call(thisObj,target,...args)});
/**
	       * Creates and returns a function which, when called, will resolve or reject
	       * the given promise based on how it is called:
	       *
	       * - If, when called, `chrome.runtime.lastError` contains a non-null object,
	       *   the promise is rejected with that value.
	       * - If the function is called with exactly one argument, the promise is
	       *   resolved to that value.
	       * - Otherwise, the promise is resolved to an array containing all of the
	       *   function's arguments.
	       *
	       * @param {object} promise
	       *        An object containing the resolution and rejection functions of a
	       *        promise.
	       * @param {function} promise.resolve
	       *        The promise's resolution function.
	       * @param {function} promise.reject
	       *        The promise's rejection function.
	       * @param {object} metadata
	       *        Metadata about the wrapped method which has created the callback.
	       * @param {boolean} metadata.singleCallbackArg
	       *        Whether or not the promise is resolved with only the first
	       *        argument of the callback, alternatively an array of all the
	       *        callback arguments is resolved. By default, if the callback
	       *        function is invoked with only a single argument, that will be
	       *        resolved to the promise, while all arguments will be resolved as
	       *        an array if multiple are given.
	       *
	       * @returns {function}
	       *        The generated callback function.
	       */let hasOwnProperty=Function.call.bind(Object.prototype.hasOwnProperty);
/**
	       * Wraps an object in a Proxy which intercepts and wraps certain methods
	       * based on the given `wrappers` and `metadata` objects.
	       *
	       * @param {object} target
	       *        The target object to wrap.
	       *
	       * @param {object} [wrappers = {}]
	       *        An object tree containing wrapper functions for special cases. Any
	       *        function present in this object tree is called in place of the
	       *        method in the same location in the `target` object tree. These
	       *        wrapper methods are invoked as described in {@see wrapMethod}.
	       *
	       * @param {object} [metadata = {}]
	       *        An object tree containing metadata used to automatically generate
	       *        Promise-based wrapper functions for asynchronous. Any function in
	       *        the `target` object tree which has a corresponding metadata object
	       *        in the same location in the `metadata` tree is replaced with an
	       *        automatically-generated wrapper function, as described in
	       *        {@see wrapAsyncFunction}
	       *
	       * @returns {Proxy<object>}
	       */const wrapObject=(target,wrappers={},metadata={})=>{let cache=Object.create(null),handlers={has:(proxyTarget,prop)=>prop in target||prop in cache,get(proxyTarget,prop,receiver){if(prop in cache)return cache[prop];if(!(prop in target))return;let value=target[prop];if("function"==typeof value)
// This is a method on the underlying object. Check if we need to do
// any wrapping.
if("function"==typeof wrappers[prop])
// We have a special-case wrapper for this method.
value=wrapMethod(target,target[prop],wrappers[prop]);else if(hasOwnProperty(metadata,prop)){
// This is an async method that we have metadata for. Create a
// Promise wrapper for it.
let wrapper=wrapAsyncFunction(prop,metadata[prop]);value=wrapMethod(target,target[prop],wrapper);}else
// This is a method that we don't know or care about. Return the
// original method, bound to the underlying object.
value=value.bind(target);else if("object"==typeof value&&null!==value&&(hasOwnProperty(wrappers,prop)||hasOwnProperty(metadata,prop)))
// This is an object that we need to do some wrapping for the children
// of. Create a sub-object wrapper for it with the appropriate child
// metadata.
value=wrapObject(value,wrappers[prop],metadata[prop]);else {if(!hasOwnProperty(metadata,"*"))
// We don't need to do any wrapping for this property,
// so just forward all access to the underlying object.
return Object.defineProperty(cache,prop,{configurable:!0,enumerable:!0,get:()=>target[prop],set(value){target[prop]=value;}}),value;
// Wrap all properties in * namespace.
value=wrapObject(value,wrappers[prop],metadata["*"]);}return cache[prop]=value,value},set:(proxyTarget,prop,value,receiver)=>(prop in cache?cache[prop]=value:target[prop]=value,!0),defineProperty:(proxyTarget,prop,desc)=>Reflect.defineProperty(cache,prop,desc),deleteProperty:(proxyTarget,prop)=>Reflect.deleteProperty(cache,prop)},proxyTarget=Object.create(target);return new Proxy(proxyTarget,handlers)},wrapEvent=wrapperMap=>({addListener(target,listener,...args){target.addListener(wrapperMap.get(listener),...args);},hasListener:(target,listener)=>target.hasListener(wrapperMap.get(listener)),removeListener(target,listener){target.removeListener(wrapperMap.get(listener));}}),onRequestFinishedWrappers=new DefaultWeakMap(listener=>"function"!=typeof listener?listener:function(req){const wrappedReq=wrapObject(req,{}
/* wrappers */,{getContent:{minArgs:0,maxArgs:0}});listener(wrappedReq);}
/**
	         * Wraps an onRequestFinished listener function so that it will return a
	         * `getContent()` property which returns a `Promise` rather than using a
	         * callback API.
	         *
	         * @param {object} req
	         *        The HAR entry object representing the network request.
	         */),onMessageWrappers=new DefaultWeakMap(listener=>"function"!=typeof listener?listener:function(message,sender,sendResponse){let wrappedSendResponse,result,didCallSendResponse=!1,sendResponsePromise=new Promise(resolve=>{wrappedSendResponse=function(response){didCallSendResponse=!0,resolve(response);};});try{result=listener(message,sender,wrappedSendResponse);}catch(err){result=Promise.reject(err);}const isResultThenable=!0!==result&&isThenable(result);// If the listener didn't returned true or a Promise, or called
// wrappedSendResponse synchronously, we can exit earlier
// because there will be no response sent from this listener.
if(!0!==result&&!isResultThenable&&!didCallSendResponse)return !1;// A small helper to send the message if the promise resolves
// and an error if the promise rejects (a wrapped sendMessage has
// to translate the message into a resolved promise or a rejected
// promise).
const sendPromisedResult=promise=>{promise.then(msg=>{
// send the message value.
sendResponse(msg);},error=>{
// Send a JSON representation of the error if the rejected value
// is an instance of error, or the object itself otherwise.
let message;message=error&&(error instanceof Error||"string"==typeof error.message)?error.message:"An unexpected error occurred",sendResponse({__mozWebExtensionPolyfillReject__:!0,message});}).catch(err=>{
// Print an error on the console if unable to send the response.
console.error("Failed to send onMessage rejected reply",err);});};// If the listener returned a Promise, send the resolved value as a
// result, otherwise wait the promise related to the wrappedSendResponse
// callback to resolve and send it as a response.
// Let Chrome know that the listener is replying.
return sendPromisedResult(isResultThenable?result:sendResponsePromise),!0}
/**
	         * Wraps a message listener function so that it may send responses based on
	         * its return value, rather than by returning a sentinel value and calling a
	         * callback. If the listener function returns a Promise, the response is
	         * sent when the promise either resolves or rejects.
	         *
	         * @param {*} message
	         *        The message sent by the other end of the channel.
	         * @param {object} sender
	         *        Details about the sender of the message.
	         * @param {function(*)} sendResponse
	         *        A callback which, when called with an arbitrary argument, sends
	         *        that value as a response.
	         * @returns {boolean}
	         *        True if the wrapped listener returned a Promise, which will later
	         *        yield a response. False otherwise.
	         */),wrappedSendMessageCallback=({reject,resolve},reply)=>{extensionAPIs.runtime.lastError?
// Detect when none of the listeners replied to the sendMessage call and resolve
// the promise to undefined as in Firefox.
// See https://github.com/mozilla/webextension-polyfill/issues/130
extensionAPIs.runtime.lastError.message===CHROME_SEND_MESSAGE_CALLBACK_NO_RESPONSE_MESSAGE?resolve():reject(new Error(extensionAPIs.runtime.lastError.message)):reply&&reply.__mozWebExtensionPolyfillReject__?
// Convert back the JSON representation of the error into
// an Error instance.
reject(new Error(reply.message)):resolve(reply);},wrappedSendMessage=(name,metadata,apiNamespaceObj,...args)=>{if(args.length<metadata.minArgs)throw new Error(`Expected at least ${metadata.minArgs} ${pluralizeArguments(metadata.minArgs)} for ${name}(), got ${args.length}`);if(args.length>metadata.maxArgs)throw new Error(`Expected at most ${metadata.maxArgs} ${pluralizeArguments(metadata.maxArgs)} for ${name}(), got ${args.length}`);return new Promise((resolve,reject)=>{const wrappedCb=wrappedSendMessageCallback.bind(null,{resolve,reject});args.push(wrappedCb),apiNamespaceObj.sendMessage(...args);})},staticWrappers={devtools:{network:{onRequestFinished:wrapEvent(onRequestFinishedWrappers)}},runtime:{onMessage:wrapEvent(onMessageWrappers),onMessageExternal:wrapEvent(onMessageWrappers),sendMessage:wrappedSendMessage.bind(null,"sendMessage",{minArgs:1,maxArgs:3})},tabs:{sendMessage:wrappedSendMessage.bind(null,"sendMessage",{minArgs:2,maxArgs:3})}},settingMetadata={clear:{minArgs:1,maxArgs:1},get:{minArgs:1,maxArgs:1},set:{minArgs:1,maxArgs:1}};
/**
	       * Creates a set of wrapper functions for an event object, which handles
	       * wrapping of listener functions that those messages are passed.
	       *
	       * A single wrapper is created for each listener function, and stored in a
	       * map. Subsequent calls to `addListener`, `hasListener`, or `removeListener`
	       * retrieve the original wrapper, so that  attempts to remove a
	       * previously-added listener work as expected.
	       *
	       * @param {DefaultWeakMap<function, function>} wrapperMap
	       *        A DefaultWeakMap object which will create the appropriate wrapper
	       *        for a given listener function when one does not exist, and retrieve
	       *        an existing one when it does.
	       *
	       * @returns {object}
	       */return apiMetadata.privacy={network:{"*":settingMetadata},services:{"*":settingMetadata},websites:{"*":settingMetadata}},wrapObject(extensionAPIs,staticWrappers,apiMetadata)};// Wrapping the bulk of this polyfill in a one-time-use function is a minor
// optimization for Firefox. Since Spidermonkey does not fully parse the
// contents of a function until the first time it's called, and since it will
// never actually need to be called, this allows the polyfill to be included
// in Firefox nearly for free.
// The build process adds a UMD wrapper around this file, which makes the
// `module` variable available.
module.exports=wrapAPIs(chrome);}else module.exports=globalThis.browser;})(browserPolyfill);var browser=getDefaultExportFromCjs(browserPolyfill.exports);class AuthenticationError extends Error{constructor(message,{cause}={}){super(message),this.name="AuthenticationError",cause&&(this.cause=cause);}}function getDaysSinceEpoch(date){return Math.floor(date.getTime()/864e5)}const rtf=new Intl.RelativeTimeFormat("en-GB",{numeric:"auto"});function formatRelative(date){const diff=getDaysSinceEpoch(date)-getDaysSinceEpoch(new Date);return rtf.format(diff,"day")}function debounce(func,wait){let timeout;return (...args)=>{clearTimeout(timeout),timeout=window.setTimeout(()=>func(...args),wait);}}async function getApiServerHost(){switch((await browser.storage.local.get({apiServer:"production"})).apiServer){case"testing":return "test-api.insite.life";case"dev":return "insite.lndo.site";default:return "api.insite.life"}}
/**
 * Retrieve from storage or request from the server an access token.
 * @throws {Error} if interaction is required.
 * TODO: implement nonce validation: https://openid.net/specs/openid-connect-basic-1_0.html#IDToken
 */const getAccessToken=function(func){let inProgress=null;return (...args)=>null!==inProgress?inProgress:inProgress=func(...args).finally(()=>{inProgress=null;})}(async function(){let lastException;try{const accessToken=await async function(){const accessToken=(await sessionStorage.get("accessToken")).accessToken;if(accessToken)return accessToken;throw new AuthenticationError("No access token")}();if(accessToken){if(o(accessToken).exp>Date.now()/1e3+2)return accessToken;await clearAccessToken();}}catch(e){lastException=e;}try{const refreshToken=await async function(){const refreshToken=(await browser.storage.local.get("refreshToken")).refreshToken;if(refreshToken)return refreshToken;throw new AuthenticationError("No refresh token")}();if(refreshToken)return await async function(refreshToken){const host=await getApiServerHost(),response=await fetch(`https://${host}/oauth/token`,{method:"POST",headers:{"Content-Type":"application/x-www-form-urlencoded"},body:new URLSearchParams([["grant_type","refresh_token"],["refresh_token",refreshToken],["client_id","chrome"]]).toString()});if(response.ok){const tokenData=await response.json();if(!tokenData.access_token)throw new AuthenticationError("No access token returned");if(!tokenData.id_token)throw new AuthenticationError("No id token returned");if(validateIdToken(tokenData.id_token,host),tokenData.refresh_token&&await writeRefreshToken(tokenData.refresh_token),tokenData.access_token)return await writeAccessToken(tokenData.access_token),tokenData.access_token}else if(401===response.status)throw await clearRefreshToken(),new AuthenticationError("Not authorized when requesting access token with refresh token");throw new AuthenticationError("Failed to refresh token")}(refreshToken)}catch(e){lastException=e;}throw new AuthenticationError("Couldn't get access token",{cause:lastException})});async function getAuthLoginUrl(){const host=await getApiServerHost(),state=(min=1,max=Number.MAX_SAFE_INTEGER,Math.floor(Math.random()*(max-min+1))+min).toString();var min,max;const redirectUrl=`https://${host}/`,params=new URLSearchParams([["response_type","code"],["client_id","chrome"],["scope",["openid","email","profile"].join(" ")],["redirect_uri",redirectUrl],["prompt","login"],["state",state]]);return await async function(stateToken){await sessionStorage.set({stateToken});}(state),new URL(`https://${host}/oauth/authorize?`+params.toString())}function validateIdToken(idTokenData,host){const idToken=o(idTokenData);if(idToken.iss!==`https://${host}/`)throw new AuthenticationError("Invalid issuer");if("chrome"!==idToken.aud)throw new AuthenticationError("Invalid audience");if(idToken.exp&&idToken.exp<Date.now()/1e3)throw new AuthenticationError("Expired token")}
/**
 * Get an access token from an authorization code.
 * @param code
 * @param state
 * @throws {Error} if the state token is invalid or the token request fails.
 */async function getAccessTokenFromCode(code,state){if(await async function(){const stateToken=(await sessionStorage.get("stateToken")).stateToken;if(stateToken)return stateToken;throw new AuthenticationError("No state token")}()!==state)throw new AuthenticationError("Invalid state");await async function(){await sessionStorage.remove("stateToken");}();const host=await getApiServerHost(),redirectUrl=`https://${host}/`;let tokenResponse;try{tokenResponse=await fetch(`https://${host}/oauth/token`,{method:"POST",body:new URLSearchParams([["grant_type","authorization_code"],["client_id","chrome"],["code",code],["redirect_uri",redirectUrl]]),headers:{"Content-Type":"application/x-www-form-urlencoded"},mode:"cors"});}catch(e){throw new AuthenticationError("Request failed",{cause:e})}if(!tokenResponse.ok)throw new AuthenticationError("Failed to get token");const tokenData=await tokenResponse.json();if(!tokenData.access_token)throw new AuthenticationError("No access token returned");if(validateIdToken(tokenData.id_token,host),tokenData.refresh_token&&await writeRefreshToken(tokenData.refresh_token),tokenData.access_token)return await writeAccessToken(tokenData.access_token),tokenData.access_token;throw new AuthenticationError("Failed to get token")}async function notifyContentScriptsOfSessionChange(token){const tabs=await browser.tabs.query({});for(const tab of tabs)if(tab.id)try{await browser.tabs.sendMessage(tab.id,{type:"session.changed",userData:token?o(token):void 0});}catch(e){}}const sessionStorage=browser.storage.session;async function writeAccessToken(accessToken){await notifyContentScriptsOfSessionChange(accessToken),await sessionStorage.set({accessToken});}async function clearAccessToken(){await notifyContentScriptsOfSessionChange(),await sessionStorage.remove("accessToken");}async function writeRefreshToken(refreshToken){await browser.storage.local.set({refreshToken});}async function clearRefreshToken(){await browser.storage.local.remove("refreshToken");}

export { AuthenticationError as A, getAuthLoginUrl as a, browser as b, getApiServerHost as c, getAccessTokenFromCode as d, clearAccessToken as e, clearRefreshToken as f, getAccessToken as g, getDefaultExportFromCjs as h, commonjsGlobal as i, formatRelative as j, debounce as k, o };
