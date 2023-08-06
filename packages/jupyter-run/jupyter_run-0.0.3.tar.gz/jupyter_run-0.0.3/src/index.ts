import { JupyterFrontEnd, JupyterFrontEndPlugin } from '@jupyterlab/application';
import { ISettingRegistry } from '@jupyterlab/settingregistry';
import { MainAreaWidget, ICommandPalette } from '@jupyterlab/apputils';
import { ILauncher } from '@jupyterlab/launcher';
import { reactIcon } from '@jupyterlab/ui-components';
import { Token } from '@lumino/coreutils';
import { DatalayerWidget } from './widget';
import { requestAPI } from './handler';
import { connect } from './ws';
import { timer, Timer, TimerView, ITimerViewProps } from "./store";

import '../style/index.css';

export type IJupyterRun = {
  timer: Timer,
  TimerView: (props: ITimerViewProps) => JSX.Element,
};

export const IJupyterRun = new Token<IJupyterRun>(
  '@datalayer/jupyter-run:plugin'
);

export const jupyterRun: IJupyterRun = {
  timer,
  TimerView,
}

/**
 * The command IDs used by the jupyter-run-widget plugin.
 */
namespace CommandIDs {
  export const create = 'create-jupyter-run-widget';
}

/**
 * Initialization data for the @datalayer/jupyter-run extension.
 */
const plugin: JupyterFrontEndPlugin<IJupyterRun> = {
  id: '@datalayer/jupyter-run:plugin',
  autoStart: true,
  requires: [ICommandPalette],
  optional: [ISettingRegistry, ILauncher],
  provides: IJupyterRun,
  activate: (
    app: JupyterFrontEnd,
    palette: ICommandPalette,
    settingRegistry: ISettingRegistry | null,
    launcher: ILauncher
  ): IJupyterRun => {
    const { commands } = app;
    const command = CommandIDs.create;
    commands.addCommand(command, {
      caption: 'Show Jupyter Run',
      label: 'Jupyter Run',
      icon: (args: any) => reactIcon,
      execute: () => {
        const content = new DatalayerWidget();
        const widget = new MainAreaWidget<DatalayerWidget>({ content });
        widget.title.label = 'Jupyter Run';
        widget.title.icon = reactIcon;
        app.shell.add(widget, 'main');
      }
    });
    const category = 'Jupyter Run';
    palette.addItem({ command, category, args: { origin: 'from palette' } });
    if (launcher) {
      launcher.add({
        command,
        category: 'Datalayer',
        rank: -1,
      });
    }
    console.log('JupyterLab extension @datalayer/jupyter-run is activated!');
    if (settingRegistry) {
      settingRegistry
        .load(plugin.id)
        .then(settings => {
          console.log('@datalayer/jupyter-run settings loaded:', settings.composite);
        })
        .catch(reason => {
          console.error('Failed to load settings for @datalayer/jupyter-run.', reason);
        });
    }
    requestAPI<any>('get_example')
      .then(data => {
        console.log(data);
      })
      .catch(reason => {
        console.error(
          `The jupyter_run server extension appears to be missing.\n${reason}`
        );
      });
    connect('ws://localhost:8888/jupyter_run/echo', true);
    return jupyterRun;
  }
};

export default plugin;
