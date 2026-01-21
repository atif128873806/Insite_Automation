import { b as browser, f as clearRefreshToken, e as clearAccessToken } from './chunks/api-d460d276.js';

/** © 2025, Insite Life Ltd. All rights reserved. **/
const apiServerElement=document.getElementById("apiserver"),themeElement=document.getElementById("theme"),saveButton=document.getElementById("save"),statusElement=document.getElementById("status");document.addEventListener("DOMContentLoaded",async()=>{const options=await browser.storage.local.get({apiServer:"production",theme:"insite"});apiServerElement&&(apiServerElement.value=options.apiServer),themeElement&&(themeElement.value=options.theme);}),saveButton.addEventListener("click",async()=>{apiServerElement&&(await browser.storage.local.set({apiServer:apiServerElement.value}),await clearRefreshToken(),await clearAccessToken()),themeElement&&await browser.storage.local.set({theme:themeElement.value}),
// Update status to let user know options were saved.
statusElement.textContent="Options saved.",setTimeout(()=>{statusElement.textContent="";},750);});
