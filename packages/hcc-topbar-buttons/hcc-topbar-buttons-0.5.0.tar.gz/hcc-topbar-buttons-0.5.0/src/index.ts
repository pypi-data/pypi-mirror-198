import { JupyterFrontEnd, JupyterFrontEndPlugin, IRouter } from '@jupyterlab/application';

import { Widget } from '@lumino/widgets';

import { ITopBar } from 'jupyterlab-topbar';

import '@jupyterlab/application/style/buttons.css';

import '../style/index.css';

const extension: JupyterFrontEndPlugin<void> = {
  id: 'jupyterlab-logout:plugin',
  autoStart: true,
  requires: [IRouter, ITopBar],
  activate: async (app: JupyterFrontEnd, router: IRouter, topBar: ITopBar) => {
    const docs = document.createElement('button');
    docs.id = 'hunt-cloud-documentation';
    docs.innerHTML = 'Documentation';
    // docs.setAttribute('style', 'padding: 0px 5px;');
    docs.addEventListener('click', () => {
      window.open('https://docs.hdc.ntnu.no/', '_blank');
    });

    const docsWidget = new Widget({ node: docs });
    docsWidget.addClass('bp3-button');
    docsWidget.addClass('bp3-minimal');
    docsWidget.addClass('minimal');
    docsWidget.addClass('jp-Button');
    docsWidget.addClass('jp-ToolbarButtonComponent');
    topBar.addItem('docs-button', docsWidget);

    const hub = document.createElement('button');
    hub.id = 'control-panel';
    hub.innerHTML = 'Control Panel';
    hub.addEventListener('click', () => {
      window.open('/hub/home', '_blank');
    });

    const hubWidget = new Widget({ node: hub });
    hubWidget.addClass('bp3-button');
    hubWidget.addClass('bp3-minimal');
    hubWidget.addClass('minimal');
    hubWidget.addClass('jp-Button');
    hubWidget.addClass('jp-ToolbarButtonComponent');
    topBar.addItem('hub-button', hubWidget);

    const logout = document.createElement('button');
    logout.id = 'logout';
    logout.type = 'button';
    logout.innerHTML = '<span class="bp3-button-text"><i aria-hidden="true" class="fa fa-sign-out"></i> Logout</span>';
    logout.addEventListener('click', () => {
      router.navigate('/logout', { hard: true });
    });

    const widget = new Widget({ node: logout });
    widget.addClass('bp3-button');
    widget.addClass('bp3-minimal');
    widget.addClass('minimal');
    widget.addClass('jp-Button');
    widget.addClass('jp-ToolbarButtonComponent');
    topBar.addItem('logout-button', widget);
  }
};

export default extension;
