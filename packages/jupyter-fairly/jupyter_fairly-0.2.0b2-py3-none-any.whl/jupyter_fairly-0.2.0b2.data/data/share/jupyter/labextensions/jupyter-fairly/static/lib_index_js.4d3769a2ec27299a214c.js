"use strict";
(self["webpackChunkjupyter_fairly"] = self["webpackChunkjupyter_fairly"] || []).push([["lib_index_js"],{

/***/ "./lib/dataset.js":
/*!************************!*\
  !*** ./lib/dataset.js ***!
  \************************/
/***/ ((__unused_webpack_module, __webpack_exports__, __webpack_require__) => {

__webpack_require__.r(__webpack_exports__);
/* harmony export */ __webpack_require__.d(__webpack_exports__, {
/* harmony export */   "cloneDatasetCommandPlugin": () => (/* binding */ cloneDatasetCommandPlugin),
/* harmony export */   "createDatasetCommandPlugin": () => (/* binding */ createDatasetCommandPlugin)
/* harmony export */ });
/* harmony import */ var _jupyterlab_ui_components__WEBPACK_IMPORTED_MODULE_0__ = __webpack_require__(/*! @jupyterlab/ui-components */ "webpack/sharing/consume/default/@jupyterlab/ui-components");
/* harmony import */ var _jupyterlab_ui_components__WEBPACK_IMPORTED_MODULE_0___default = /*#__PURE__*/__webpack_require__.n(_jupyterlab_ui_components__WEBPACK_IMPORTED_MODULE_0__);
/* harmony import */ var _jupyterlab_apputils__WEBPACK_IMPORTED_MODULE_1__ = __webpack_require__(/*! @jupyterlab/apputils */ "webpack/sharing/consume/default/@jupyterlab/apputils");
/* harmony import */ var _jupyterlab_apputils__WEBPACK_IMPORTED_MODULE_1___default = /*#__PURE__*/__webpack_require__.n(_jupyterlab_apputils__WEBPACK_IMPORTED_MODULE_1__);
/* harmony import */ var _jupyterlab_filebrowser__WEBPACK_IMPORTED_MODULE_2__ = __webpack_require__(/*! @jupyterlab/filebrowser */ "webpack/sharing/consume/default/@jupyterlab/filebrowser");
/* harmony import */ var _jupyterlab_filebrowser__WEBPACK_IMPORTED_MODULE_2___default = /*#__PURE__*/__webpack_require__.n(_jupyterlab_filebrowser__WEBPACK_IMPORTED_MODULE_2__);
/* harmony import */ var _handler__WEBPACK_IMPORTED_MODULE_3__ = __webpack_require__(/*! ./handler */ "./lib/handler.js");
/* harmony import */ var _widgets_CloneForm__WEBPACK_IMPORTED_MODULE_4__ = __webpack_require__(/*! ./widgets/CloneForm */ "./lib/widgets/CloneForm.js");
/* harmony import */ var _logger__WEBPACK_IMPORTED_MODULE_5__ = __webpack_require__(/*! ./logger */ "./lib/logger.js");
/* harmony import */ var _tokens__WEBPACK_IMPORTED_MODULE_6__ = __webpack_require__(/*! ./tokens */ "./lib/tokens.js");







// import handlers from Jupyter Server extension
// import { initDataset } from './fairly-api';
function initDataset(path, template) {
    /**
     * Initializes a Fairly dataset
     * @param path - path to dataset root directory. Default to current path
     * @param template - alias of template for manifest.yalm
     */
    // name of the template for manifest.yalm
    let templateMeta = '';
    /* ./ is necessary becaucause defaultBrowser.Model.path
    * returns an empty string when fileBlowser is on the
    * jupyterlab root directory
    */
    let rootPath = './';
    if (template === '4TU.Research' || template === 'Figshare') {
        templateMeta = 'figshare';
    }
    else if (template === 'Zenodo') {
        templateMeta = 'zenodo';
    }
    else if (template == null || template === 'Default') {
        templateMeta = 'default';
    }
    console.log(rootPath.concat(path));
    (0,_handler__WEBPACK_IMPORTED_MODULE_3__.requestAPI)('newdataset', {
        method: 'POST',
        body: JSON.stringify({
            path: rootPath.concat(path),
            template: templateMeta
        })
    })
        .then(data => {
        console.log(data);
    })
        .catch(reason => {
        console.error(`${reason}`);
        // show error when manifest.yalm already exist in rootPath
        (0,_jupyterlab_apputils__WEBPACK_IMPORTED_MODULE_1__.showErrorMessage)("Error: Has the dataset been initilized already?", reason);
    });
}
function cloneDataset(source, destination, client) {
    /**
     * clones a remote dataset to a directory
     * @param source - DOI or URL to the remote dataset
     * @param destination - realtive path to a directory to store the dataset
     * @param client - fairly client
     */
    /* ./ is necessary becaucause defaultBrowser.Model.path
    * returns an empty string when fileBlowser is on the
    * jupyterlab root directory
    */
    let rootPath = './';
    let _client = '4tu';
    let payload = JSON.stringify({
        source: source,
        destination: rootPath.concat(destination),
        client: _client
    });
    console.log(rootPath.concat(destination));
    (0,_handler__WEBPACK_IMPORTED_MODULE_3__.requestAPI)('clone', {
        method: 'POST',
        body: payload
    })
        .then(data => {
        console.log(data);
    })
        .catch(reason => {
        // show error when destination directory is not empty
        (0,_jupyterlab_apputils__WEBPACK_IMPORTED_MODULE_1__.showErrorMessage)("Error when cloning dataset", reason);
    });
}
const cloneDatasetCommandPlugin = {
    id: 'jupyter-fairly:clone',
    requires: [_jupyterlab_filebrowser__WEBPACK_IMPORTED_MODULE_2__.IFileBrowserFactory],
    autoStart: true,
    activate: (app, fileBrowserFactory) => {
        console.log("cloneDatasetCommandPlugin activated!!");
        const fileBrowser = fileBrowserFactory.defaultBrowser;
        const fileBrowserModel = fileBrowser.model;
        const cloneDatasetCommand = "cloneDatasetCommand";
        app.commands.addCommand(cloneDatasetCommand, {
            label: 'Clone Dataset',
            isEnabled: () => true,
            isVisible: () => true,
            icon: _jupyterlab_ui_components__WEBPACK_IMPORTED_MODULE_0__.downloadIcon,
            execute: async () => {
                const result = await (0,_jupyterlab_apputils__WEBPACK_IMPORTED_MODULE_1__.showDialog)({
                    title: 'Clone Dataset',
                    body: new _widgets_CloneForm__WEBPACK_IMPORTED_MODULE_4__.FairlyCloneForm(),
                    buttons: [
                        _jupyterlab_apputils__WEBPACK_IMPORTED_MODULE_1__.Dialog.cancelButton({ label: 'Cancel' }),
                        _jupyterlab_apputils__WEBPACK_IMPORTED_MODULE_1__.Dialog.okButton({ label: 'Clone' })
                    ]
                });
                if (result.button.accept && result.value) {
                    _logger__WEBPACK_IMPORTED_MODULE_5__.logger.log({
                        level: _tokens__WEBPACK_IMPORTED_MODULE_6__.Level.RUNNING,
                        message: 'Cloning...'
                    });
                    try {
                        cloneDataset(result.value, fileBrowserModel.path);
                        console.log('accepted');
                        await fileBrowserModel.refresh();
                    }
                    catch (error) {
                        console.error('Encontered an error when cloning the dataset: ', error);
                    }
                }
                else {
                    console.log('rejected');
                }
            }
        });
        app.contextMenu.addItem({
            command: cloneDatasetCommand,
            // matches anywhere in the filebrowser
            selector: '.jp-DirListing-content',
            rank: 106
        });
    }
};
const createDatasetCommandPlugin = {
    id: 'jupyter-fairly:create-dataset',
    requires: [_jupyterlab_filebrowser__WEBPACK_IMPORTED_MODULE_2__.IFileBrowserFactory],
    autoStart: true,
    activate: (app, fileBrowserFactory) => {
        console.log("createDatasetCommandPlugin activated!!");
        const fileBrowser = fileBrowserFactory.defaultBrowser;
        const fileBrowserModel = fileBrowser.model;
        const createDatasetCommand = "createDatasetCommand";
        // TODO: find how to use notifications and actions
        // to promp user on execution of some commands.
        app.commands.execute('apputils:notify', {
            message: 'initilize dataset',
            type: 'info',
            options: {
                autoClose: false,
                actions: {
                    label: 'notification init',
                    commandId: createDatasetCommand,
                }
            }
        });
        //  {
        //   /**
        //    * The action label.
        //    *
        //    * This should be a short description.
        //    */
        //   label: string;
        //   /**
        //    * Callback command id to trigger
        //    */
        //   commandId: string;
        //   /**
        //    * Command arguments
        //    */
        //   args?: ReadonlyJsonObject;
        //   /**
        //    * The action caption.
        //    *
        //    * This can be a longer description of the action.
        //    */
        //   caption?: string;
        // }
        app.commands.addCommand(createDatasetCommand, {
            label: 'Create Fairly Dataset',
            isEnabled: () => true,
            isVisible: () => true,
            icon: _jupyterlab_ui_components__WEBPACK_IMPORTED_MODULE_0__.addIcon,
            execute: async () => {
                // return relative path w.r.t. jupyter root path.
                // root-path = empty string.
                console.log(`the path is: ${fileBrowserModel.path}`);
                let metadataTemplate = await _jupyterlab_apputils__WEBPACK_IMPORTED_MODULE_1__.InputDialog.getItem({
                    title: 'Select template for dataset\'s metadata',
                    items: ['', 'Default', '4TU.Research', 'Zenodo', 'Figshare'],
                    okLabel: 'Create',
                });
                // initialize dataset when accept button is clicked and 
                // vaule for teamplate is not null
                if (metadataTemplate.button.accept && metadataTemplate.value) {
                    console.log(`the path is: ${fileBrowserModel.path}`);
                    initDataset(fileBrowserModel.path, metadataTemplate.value);
                    await fileBrowserModel.refresh();
                }
                else {
                    console.log('rejected');
                    return;
                }
            }
        });
        app.contextMenu.addItem({
            command: createDatasetCommand,
            // matches anywhere in the filebrowser
            selector: '.jp-DirListing-content',
            rank: 100
        });
    }
};
///
// function initDataset(rootPath:string, template: any) {
//   requestAPI<any>('newdataset', {
//     method: 'POST', 
//     body: JSON.stringify({
//       path: rootPath, 
//       template: template
//     })
//   }) // This is how to query the api-url
//   .then(data => {
//     console.log(data);
//   })
//   .catch(reason => {
//     console.error(
//       `The jupyter-fairly server extension appears to be missing.\n${reason}`
//     );
//   });
// }
// const fbModel = new FilterFileBrowserModel({ manager: docManager});
// const fbWidget = new FileBrowser({
//   id: 'filebrowser',
//   model: 
// };
// const browser = factory.tracker.currentWidget;
// console.log(browser);
// const basePath = factory.defaultBrowser.model.path;
// // const basePath = factory.tracker.;
// console.log(`workspace: ${basePath}`);
// const {tracker} = factory;


/***/ }),

/***/ "./lib/handler.js":
/*!************************!*\
  !*** ./lib/handler.js ***!
  \************************/
/***/ ((__unused_webpack_module, __webpack_exports__, __webpack_require__) => {

__webpack_require__.r(__webpack_exports__);
/* harmony export */ __webpack_require__.d(__webpack_exports__, {
/* harmony export */   "requestAPI": () => (/* binding */ requestAPI)
/* harmony export */ });
/* harmony import */ var _jupyterlab_coreutils__WEBPACK_IMPORTED_MODULE_0__ = __webpack_require__(/*! @jupyterlab/coreutils */ "webpack/sharing/consume/default/@jupyterlab/coreutils");
/* harmony import */ var _jupyterlab_coreutils__WEBPACK_IMPORTED_MODULE_0___default = /*#__PURE__*/__webpack_require__.n(_jupyterlab_coreutils__WEBPACK_IMPORTED_MODULE_0__);
/* harmony import */ var _jupyterlab_services__WEBPACK_IMPORTED_MODULE_1__ = __webpack_require__(/*! @jupyterlab/services */ "webpack/sharing/consume/default/@jupyterlab/services");
/* harmony import */ var _jupyterlab_services__WEBPACK_IMPORTED_MODULE_1___default = /*#__PURE__*/__webpack_require__.n(_jupyterlab_services__WEBPACK_IMPORTED_MODULE_1__);


/**
 * Call the API extension
 *
 * @param endPoint API REST end point for the extension
 * @param init Initial values for the request
 * @returns The response body interpreted as JSON
 */
async function requestAPI(endPoint = '', init = {}) {
    // Make request to Jupyter API
    const settings = _jupyterlab_services__WEBPACK_IMPORTED_MODULE_1__.ServerConnection.makeSettings();
    const requestUrl = _jupyterlab_coreutils__WEBPACK_IMPORTED_MODULE_0__.URLExt.join(settings.baseUrl, 'jupyter-fairly', // API Namespace
    endPoint);
    let response;
    try {
        response = await _jupyterlab_services__WEBPACK_IMPORTED_MODULE_1__.ServerConnection.makeRequest(requestUrl, init, settings);
    }
    catch (error) {
        throw new _jupyterlab_services__WEBPACK_IMPORTED_MODULE_1__.ServerConnection.NetworkError(error);
    }
    let data = await response.text();
    if (data.length > 0) {
        try {
            data = JSON.parse(data);
        }
        catch (error) {
            console.log('Not a JSON response body.', response);
        }
    }
    if (!response.ok) {
        throw new _jupyterlab_services__WEBPACK_IMPORTED_MODULE_1__.ServerConnection.ResponseError(response, data.message || data);
    }
    return data;
}


/***/ }),

/***/ "./lib/index.js":
/*!**********************!*\
  !*** ./lib/index.js ***!
  \**********************/
/***/ ((__unused_webpack_module, __webpack_exports__, __webpack_require__) => {

__webpack_require__.r(__webpack_exports__);
/* harmony export */ __webpack_require__.d(__webpack_exports__, {
/* harmony export */   "default": () => (__WEBPACK_DEFAULT_EXPORT__)
/* harmony export */ });
/* harmony import */ var _jupyterlab_settingregistry__WEBPACK_IMPORTED_MODULE_0__ = __webpack_require__(/*! @jupyterlab/settingregistry */ "webpack/sharing/consume/default/@jupyterlab/settingregistry");
/* harmony import */ var _jupyterlab_settingregistry__WEBPACK_IMPORTED_MODULE_0___default = /*#__PURE__*/__webpack_require__.n(_jupyterlab_settingregistry__WEBPACK_IMPORTED_MODULE_0__);
/* harmony import */ var _jupyterlab_apputils__WEBPACK_IMPORTED_MODULE_1__ = __webpack_require__(/*! @jupyterlab/apputils */ "webpack/sharing/consume/default/@jupyterlab/apputils");
/* harmony import */ var _jupyterlab_apputils__WEBPACK_IMPORTED_MODULE_1___default = /*#__PURE__*/__webpack_require__.n(_jupyterlab_apputils__WEBPACK_IMPORTED_MODULE_1__);
/* harmony import */ var _dataset__WEBPACK_IMPORTED_MODULE_2__ = __webpack_require__(/*! ./dataset */ "./lib/dataset.js");
/* harmony import */ var _metadata__WEBPACK_IMPORTED_MODULE_3__ = __webpack_require__(/*! ./metadata */ "./lib/metadata.js");
/* harmony import */ var _upload__WEBPACK_IMPORTED_MODULE_4__ = __webpack_require__(/*! ./upload */ "./lib/upload.js");





// import { FairlyWidget } from './widgets/FairlyTab';
/**
 *  Activate jupyter-fairly extension.
 */
const plugin = {
    id: 'jupyter-fairly:plugin',
    autoStart: true,
    requires: [_jupyterlab_apputils__WEBPACK_IMPORTED_MODULE_1__.ICommandPalette],
    optional: [_jupyterlab_settingregistry__WEBPACK_IMPORTED_MODULE_0__.ISettingRegistry],
    activate: (app, palette, settingRegistry) => {
        console.log('jupytefair is activated!!');
        // this doesn't do what is expected
        // See: https://stackoverflow.com/questions/63065310/how-do-i-create-a-jupyter-lab-extension-that-adds-a-custom-button-to-the-toolba
        const openFairlyTabCommand = 'widgets:open-tab';
        app.commands.addCommand(openFairlyTabCommand, {
            label: 'Open Fairly Tab',
            caption: 'Open the Fairly Tab',
            // isEnabled: () => true,
            // isVisible: () => true,
            execute: () => {
                // const widget = new FairlyWidget();
                // app.shell.add(widget, 'main');
            }
        });
        palette.addItem({ command: openFairlyTabCommand, category: 'Fairly' });
    }
};
/* harmony default export */ const __WEBPACK_DEFAULT_EXPORT__ = ([
    plugin,
    _dataset__WEBPACK_IMPORTED_MODULE_2__.createDatasetCommandPlugin,
    _metadata__WEBPACK_IMPORTED_MODULE_3__.editMetadataPlugin,
    _upload__WEBPACK_IMPORTED_MODULE_4__.uploadDatasetPlugin,
    _dataset__WEBPACK_IMPORTED_MODULE_2__.cloneDatasetCommandPlugin
]);
//Todo: add new tab to left pannel
// example: https://github.com/jupyterlab/extension-examples/tree/master/widgets


/***/ }),

/***/ "./lib/logger.js":
/*!***********************!*\
  !*** ./lib/logger.js ***!
  \***********************/
/***/ ((__unused_webpack_module, __webpack_exports__, __webpack_require__) => {

__webpack_require__.r(__webpack_exports__);
/* harmony export */ __webpack_require__.d(__webpack_exports__, {
/* harmony export */   "Logger": () => (/* binding */ Logger),
/* harmony export */   "LoggerContext": () => (/* binding */ LoggerContext),
/* harmony export */   "logger": () => (/* binding */ logger)
/* harmony export */ });
/* harmony import */ var react__WEBPACK_IMPORTED_MODULE_0__ = __webpack_require__(/*! react */ "webpack/sharing/consume/default/react");
/* harmony import */ var react__WEBPACK_IMPORTED_MODULE_0___default = /*#__PURE__*/__webpack_require__.n(react__WEBPACK_IMPORTED_MODULE_0__);
/* harmony import */ var _lumino_signaling__WEBPACK_IMPORTED_MODULE_1__ = __webpack_require__(/*! @lumino/signaling */ "webpack/sharing/consume/default/@lumino/signaling");
/* harmony import */ var _lumino_signaling__WEBPACK_IMPORTED_MODULE_1___default = /*#__PURE__*/__webpack_require__.n(_lumino_signaling__WEBPACK_IMPORTED_MODULE_1__);


/**
 * Logger
 */
class Logger {
    constructor() {
        this._signal = new _lumino_signaling__WEBPACK_IMPORTED_MODULE_1__.Signal(this);
    }
    /**
     * Signal emitted when a log message is sent
     */
    get signal() {
        return this._signal;
    }
    /**
     * Send a log message.
     *
     * @param message Log message
     */
    log(message) {
        this._signal.emit(message);
    }
}
/**
 * Default logger
 */
const logger = new Logger();
/**
 * Default logger context for React
 */
const LoggerContext = react__WEBPACK_IMPORTED_MODULE_0__.createContext(logger);


/***/ }),

/***/ "./lib/metadata.js":
/*!*************************!*\
  !*** ./lib/metadata.js ***!
  \*************************/
/***/ ((__unused_webpack_module, __webpack_exports__, __webpack_require__) => {

__webpack_require__.r(__webpack_exports__);
/* harmony export */ __webpack_require__.d(__webpack_exports__, {
/* harmony export */   "editMetadataPlugin": () => (/* binding */ editMetadataPlugin)
/* harmony export */ });
/* harmony import */ var _jupyterlab_ui_components__WEBPACK_IMPORTED_MODULE_0__ = __webpack_require__(/*! @jupyterlab/ui-components */ "webpack/sharing/consume/default/@jupyterlab/ui-components");
/* harmony import */ var _jupyterlab_ui_components__WEBPACK_IMPORTED_MODULE_0___default = /*#__PURE__*/__webpack_require__.n(_jupyterlab_ui_components__WEBPACK_IMPORTED_MODULE_0__);
/* harmony import */ var _jupyterlab_filebrowser__WEBPACK_IMPORTED_MODULE_1__ = __webpack_require__(/*! @jupyterlab/filebrowser */ "webpack/sharing/consume/default/@jupyterlab/filebrowser");
/* harmony import */ var _jupyterlab_filebrowser__WEBPACK_IMPORTED_MODULE_1___default = /*#__PURE__*/__webpack_require__.n(_jupyterlab_filebrowser__WEBPACK_IMPORTED_MODULE_1__);
/* harmony import */ var _jupyterlab_apputils__WEBPACK_IMPORTED_MODULE_2__ = __webpack_require__(/*! @jupyterlab/apputils */ "webpack/sharing/consume/default/@jupyterlab/apputils");
/* harmony import */ var _jupyterlab_apputils__WEBPACK_IMPORTED_MODULE_2___default = /*#__PURE__*/__webpack_require__.n(_jupyterlab_apputils__WEBPACK_IMPORTED_MODULE_2__);



const editMetadataPlugin = {
    id: 'jupyter-fairly:edit-meta',
    requires: [_jupyterlab_filebrowser__WEBPACK_IMPORTED_MODULE_1__.IFileBrowserFactory],
    autoStart: true,
    activate: (app, fileBrowserFactory) => {
        console.log("editMetadataPlugin activated!!");
        const fileBrowser = fileBrowserFactory.defaultBrowser;
        const fileBrowserModel = fileBrowser.model;
        // Open the manifest.yalm file in the file editor
        const openManifestCommand = "openManifestCommand";
        app.commands.addCommand(openManifestCommand, {
            label: 'Edit Dataset Metadata',
            isEnabled: () => true,
            isVisible: () => true,
            icon: _jupyterlab_ui_components__WEBPACK_IMPORTED_MODULE_0__.editIcon,
            execute: () => {
                let currentPath = './'.concat(fileBrowserModel.path);
                const pathManifest = currentPath.concat('/manifest.yaml');
                /* We assume that the current directory contains the
                manifest.yalm, if not we show an error message
                 */
                try {
                    fileBrowserModel.manager.open(pathManifest);
                }
                catch (error) {
                    // TODO: customize error type
                    (0,_jupyterlab_apputils__WEBPACK_IMPORTED_MODULE_2__.showErrorMessage)("Error Opening manifest.yalm", error);
                }
                ;
            }
        });
        app.contextMenu.addItem({
            command: openManifestCommand,
            // matches anywhere in the filebrowser
            selector: '.jp-DirListing-content',
            rank: 105
        });
    }
};


/***/ }),

/***/ "./lib/tokens.js":
/*!***********************!*\
  !*** ./lib/tokens.js ***!
  \***********************/
/***/ ((__unused_webpack_module, __webpack_exports__, __webpack_require__) => {

__webpack_require__.r(__webpack_exports__);
/* harmony export */ __webpack_require__.d(__webpack_exports__, {
/* harmony export */   "CommandIDs": () => (/* binding */ CommandIDs),
/* harmony export */   "ContextCommandIDs": () => (/* binding */ ContextCommandIDs),
/* harmony export */   "EXTENSION_ID": () => (/* binding */ EXTENSION_ID),
/* harmony export */   "Git": () => (/* binding */ Git),
/* harmony export */   "IGitExtension": () => (/* binding */ IGitExtension),
/* harmony export */   "Level": () => (/* binding */ Level)
/* harmony export */ });
/* harmony import */ var _jupyterlab_services__WEBPACK_IMPORTED_MODULE_0__ = __webpack_require__(/*! @jupyterlab/services */ "webpack/sharing/consume/default/@jupyterlab/services");
/* harmony import */ var _jupyterlab_services__WEBPACK_IMPORTED_MODULE_0___default = /*#__PURE__*/__webpack_require__.n(_jupyterlab_services__WEBPACK_IMPORTED_MODULE_0__);
/* harmony import */ var _lumino_coreutils__WEBPACK_IMPORTED_MODULE_1__ = __webpack_require__(/*! @lumino/coreutils */ "webpack/sharing/consume/default/@lumino/coreutils");
/* harmony import */ var _lumino_coreutils__WEBPACK_IMPORTED_MODULE_1___default = /*#__PURE__*/__webpack_require__.n(_lumino_coreutils__WEBPACK_IMPORTED_MODULE_1__);


const EXTENSION_ID = 'jupyter.extensions.git_plugin';
const IGitExtension = new _lumino_coreutils__WEBPACK_IMPORTED_MODULE_1__.Token(EXTENSION_ID);
var Git;
(function (Git) {
    let Diff;
    (function (Diff) {
        let SpecialRef;
        (function (SpecialRef) {
            // Working version
            SpecialRef[SpecialRef["WORKING"] = 0] = "WORKING";
            // Index version
            SpecialRef[SpecialRef["INDEX"] = 1] = "INDEX";
            // Common ancestor version (useful for unmerged files)
            SpecialRef[SpecialRef["BASE"] = 2] = "BASE";
        })(SpecialRef = Diff.SpecialRef || (Diff.SpecialRef = {}));
    })(Diff = Git.Diff || (Git.Diff = {}));
    /**
     * A wrapped error for a fetch response.
     */
    class GitResponseError extends _jupyterlab_services__WEBPACK_IMPORTED_MODULE_0__.ServerConnection.ResponseError {
        /**
         * Create a new response error.
         */
        constructor(response, message = `Invalid response: ${response.status} ${response.statusText}`, traceback = '', json = {}) {
            super(response, message);
            this.traceback = traceback; // traceback added in mother class in 2.2.x
            this._json = json;
        }
        /**
         * The error response JSON body
         */
        get json() {
            return this._json;
        }
    }
    Git.GitResponseError = GitResponseError;
    class NotInRepository extends Error {
        constructor() {
            super('Not in a Git Repository');
        }
    }
    Git.NotInRepository = NotInRepository;
})(Git || (Git = {}));
/**
 * Log message severity.
 */
var Level;
(function (Level) {
    Level[Level["SUCCESS"] = 10] = "SUCCESS";
    Level[Level["INFO"] = 20] = "INFO";
    Level[Level["RUNNING"] = 30] = "RUNNING";
    Level[Level["WARNING"] = 40] = "WARNING";
    Level[Level["ERROR"] = 50] = "ERROR";
})(Level || (Level = {}));
/**
 * The command IDs used in the git context menus.
 */
var ContextCommandIDs;
(function (ContextCommandIDs) {
    ContextCommandIDs["gitCommitAmendStaged"] = "git:context-commitAmendStaged";
    ContextCommandIDs["gitFileAdd"] = "git:context-add";
    ContextCommandIDs["gitFileDiff"] = "git:context-diff";
    ContextCommandIDs["gitFileDiscard"] = "git:context-discard";
    ContextCommandIDs["gitFileDelete"] = "git:context-delete";
    ContextCommandIDs["gitFileOpen"] = "git:context-open";
    ContextCommandIDs["gitFileUnstage"] = "git:context-unstage";
    ContextCommandIDs["gitFileStage"] = "git:context-stage";
    ContextCommandIDs["gitFileTrack"] = "git:context-track";
    ContextCommandIDs["gitFileHistory"] = "git:context-history";
    ContextCommandIDs["gitIgnore"] = "git:context-ignore";
    ContextCommandIDs["gitIgnoreExtension"] = "git:context-ignoreExtension";
    ContextCommandIDs["gitNoAction"] = "git:no-action";
    ContextCommandIDs["openFileFromDiff"] = "git:open-file-from-diff";
})(ContextCommandIDs || (ContextCommandIDs = {}));
/**
 * The command IDs used by the git plugin.
 */
var CommandIDs;
(function (CommandIDs) {
    CommandIDs["gitUI"] = "git:ui";
    CommandIDs["gitTerminalCommand"] = "git:terminal-command";
    CommandIDs["gitInit"] = "git:init";
    CommandIDs["gitOpenUrl"] = "git:open-url";
    CommandIDs["gitToggleSimpleStaging"] = "git:toggle-simple-staging";
    CommandIDs["gitToggleDoubleClickDiff"] = "git:toggle-double-click-diff";
    CommandIDs["gitManageRemote"] = "git:manage-remote";
    CommandIDs["gitClone"] = "git:clone";
    CommandIDs["gitMerge"] = "git:merge";
    CommandIDs["gitOpenGitignore"] = "git:open-gitignore";
    CommandIDs["gitPush"] = "git:push";
    CommandIDs["gitPull"] = "git:pull";
    CommandIDs["gitResetToRemote"] = "git:reset-to-remote";
    CommandIDs["gitSubmitCommand"] = "git:submit-commit";
    CommandIDs["gitShowDiff"] = "git:show-diff";
})(CommandIDs || (CommandIDs = {}));


/***/ }),

/***/ "./lib/upload.js":
/*!***********************!*\
  !*** ./lib/upload.js ***!
  \***********************/
/***/ ((__unused_webpack_module, __webpack_exports__, __webpack_require__) => {

__webpack_require__.r(__webpack_exports__);
/* harmony export */ __webpack_require__.d(__webpack_exports__, {
/* harmony export */   "uploadDatasetPlugin": () => (/* binding */ uploadDatasetPlugin)
/* harmony export */ });
/* harmony import */ var _jupyterlab_apputils__WEBPACK_IMPORTED_MODULE_0__ = __webpack_require__(/*! @jupyterlab/apputils */ "webpack/sharing/consume/default/@jupyterlab/apputils");
/* harmony import */ var _jupyterlab_apputils__WEBPACK_IMPORTED_MODULE_0___default = /*#__PURE__*/__webpack_require__.n(_jupyterlab_apputils__WEBPACK_IMPORTED_MODULE_0__);
/* harmony import */ var _jupyterlab_filebrowser__WEBPACK_IMPORTED_MODULE_1__ = __webpack_require__(/*! @jupyterlab/filebrowser */ "webpack/sharing/consume/default/@jupyterlab/filebrowser");
/* harmony import */ var _jupyterlab_filebrowser__WEBPACK_IMPORTED_MODULE_1___default = /*#__PURE__*/__webpack_require__.n(_jupyterlab_filebrowser__WEBPACK_IMPORTED_MODULE_1__);
/* harmony import */ var _jupyterlab_ui_components__WEBPACK_IMPORTED_MODULE_2__ = __webpack_require__(/*! @jupyterlab/ui-components */ "webpack/sharing/consume/default/@jupyterlab/ui-components");
/* harmony import */ var _jupyterlab_ui_components__WEBPACK_IMPORTED_MODULE_2___default = /*#__PURE__*/__webpack_require__.n(_jupyterlab_ui_components__WEBPACK_IMPORTED_MODULE_2__);
/* harmony import */ var _handler__WEBPACK_IMPORTED_MODULE_3__ = __webpack_require__(/*! ./handler */ "./lib/handler.js");


// Icons



/**
 * Uploads metadata and files to data repository
 */
function uploadDataset(directory, repository) {
    /**
     * upload local dataset to data reposotory
     * @param directory - realtive path to directory of local dataset
     * @param repository - name of data repository
     */
    /* ./ is necessary becaucause defaultBrowser.Model.path
    * returns an empty string when fileBlowser is on the
    * jupyterlab root directory
    */
    let rootPath = './';
    var client;
    if (repository === '4TU.ResearchData') {
        client = '4tu';
    }
    else if (repository === 'Zenodo') {
        client = 'zenodo';
    }
    else if (repository === 'Figshare') {
        client = 'figshare';
    }
    ;
    let payload = JSON.stringify({
        directory: rootPath.concat(directory),
        client: client
    });
    console.log(payload);
    (0,_handler__WEBPACK_IMPORTED_MODULE_3__.requestAPI)('upload', {
        method: 'POST',
        body: payload
    })
        .then(data => {
        console.log(data);
    })
        .catch(reason => {
        // show error when 
        (0,_jupyterlab_apputils__WEBPACK_IMPORTED_MODULE_0__.showErrorMessage)("Error when uploading dataset", reason);
    });
}
;
const uploadDatasetPlugin = {
    id: 'jupyter-fairly:upload',
    requires: [_jupyterlab_filebrowser__WEBPACK_IMPORTED_MODULE_1__.IFileBrowserFactory],
    autoStart: true,
    activate: (app, fileBrowserFactory) => {
        console.log("uploadDatasetPlugin activated!!");
        const fileBrowser = fileBrowserFactory.defaultBrowser;
        const fileBrowserModel = fileBrowser.model;
        // TODO: the plugin start without error, but the model.path is an empty string for root-path (path where jupyter was started.)
        const archiveDatasetCommand = "uploadDataset";
        app.commands.addCommand(archiveDatasetCommand, {
            label: 'Upload Dataset',
            isEnabled: () => true,
            isVisible: () => true,
            icon: _jupyterlab_ui_components__WEBPACK_IMPORTED_MODULE_2__.fileUploadIcon,
            execute: async () => {
                // return relative path w.r.t. jupyterlab root path.
                // root-path = empty string.
                console.log(`the path is: ${fileBrowserModel.path}`);
                let targetRepository = await _jupyterlab_apputils__WEBPACK_IMPORTED_MODULE_0__.InputDialog.getItem({
                    title: 'Select Data Repository',
                    items: ['4TU.ResearchData', 'Zenodo', 'Figshare'],
                    okLabel: 'Continue',
                });
                // initialize dataset when accept button is clicked and 
                // vaule for teamplate is not null
                if (targetRepository.button.accept && targetRepository.value) {
                    let confirmAction = await _jupyterlab_apputils__WEBPACK_IMPORTED_MODULE_0__.InputDialog.getBoolean({
                        title: 'Do you want to upload the dataset?',
                        label: `Yes, upload metadata and files to ${targetRepository.value}`
                    });
                    if (confirmAction.button.accept) {
                        console.log('uploading dataset');
                        uploadDataset(fileBrowserModel.path, targetRepository.value);
                    }
                    else {
                        console.log('do not archive');
                        return;
                    }
                    ;
                }
                else {
                    console.log('rejected');
                    return;
                }
            }
        });
        app.contextMenu.addItem({
            command: archiveDatasetCommand,
            // matches anywhere in the filebrowser
            selector: '.jp-DirListing-content',
            rank: 102
        });
    }
};
///
// function initDataset(rootPath:string, template: any) {
//   requestAPI<any>('newdataset', {
//     method: 'POST', 
//     body: JSON.stringify({
//       path: rootPath, 
//       template: template
//     })
//   }) // This is how to query the api-url
//   .then(data => {
//     console.log(data);
//   })
//   .catch(reason => {
//     console.error(
//       `The jupyter-fairly server extension appears to be missing.\n${reason}`
//     );
//   });
// }
// const fbModel = new FilterFileBrowserModel({ manager: docManager});
// const fbWidget = new FileBrowser({
//   id: 'filebrowser',
//   model: 
// };
// const browser = factory.tracker.currentWidget;
// console.log(browser);
// const basePath = factory.defaultBrowser.model.path;
// // const basePath = factory.tracker.;
// console.log(`workspace: ${basePath}`);
// const {tracker} = factory;


/***/ }),

/***/ "./lib/widgets/CloneForm.js":
/*!**********************************!*\
  !*** ./lib/widgets/CloneForm.js ***!
  \**********************************/
/***/ ((__unused_webpack_module, __webpack_exports__, __webpack_require__) => {

__webpack_require__.r(__webpack_exports__);
/* harmony export */ __webpack_require__.d(__webpack_exports__, {
/* harmony export */   "FairlyCloneForm": () => (/* binding */ FairlyCloneForm)
/* harmony export */ });
/* harmony import */ var _lumino_widgets__WEBPACK_IMPORTED_MODULE_0__ = __webpack_require__(/*! @lumino/widgets */ "webpack/sharing/consume/default/@lumino/widgets");
/* harmony import */ var _lumino_widgets__WEBPACK_IMPORTED_MODULE_0___default = /*#__PURE__*/__webpack_require__.n(_lumino_widgets__WEBPACK_IMPORTED_MODULE_0__);

/**
 * The UI for the form fields shown within the Clone modal.
 */
class FairlyCloneForm extends _lumino_widgets__WEBPACK_IMPORTED_MODULE_0__.Widget {
    /**
     * Creates a form for cloning datasets
     *
     */
    constructor() {
        super({ node: FairlyCloneForm.createFormNode() });
    }
    /**
     * Returns the input value as plain text
     */
    getValue() {
        // TODO: this should be properly initialized, 
        // See: https://stackoverflow.com/questions/40349987/how-to-suppress-error-ts2533-object-is-possibly-null-or-undefined
        return this.node.querySelector('input').value.trim(); // strickNullChecks = true, brakes this code
    }
    static createFormNode() {
        const node = document.createElement('div');
        const label = document.createElement('label');
        const input = document.createElement('input');
        const text = document.createElement('span');
        node.className = 'jp-RedirectForm';
        text.textContent = 'Enter the URL or DOI of the dataset';
        input.placeholder = 'https://doi.org/xx.x/xx.vx';
        label.appendChild(text);
        label.appendChild(input);
        node.appendChild(label);
        return node;
    }
}


/***/ })

}]);
//# sourceMappingURL=lib_index_js.4d3769a2ec27299a214c.js.map