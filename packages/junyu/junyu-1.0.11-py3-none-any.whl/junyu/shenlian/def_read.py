"""
根据筛选出来的(project, layer, date)，读取def文件和tag信息，def_red返回fig和position，tag_read返回tag
"""

import os
import numpy as np
from . import mudeConstant as mc


def def_read(path):
    """
    :param path: def文件路径
    :return: fig: dict，每个元素为np.array图片； position: dict，每个元素为坐标元组
    """
    files = os.listdir(path)
    files = set([os.path.splitext(file)[0] for file in files if os.path.isfile(os.path.join(path, file))])
    files = [int(file.split('_')[-1]) for file in files]
    files.sort()

    fig, position = {}, {}
    t = path.split('\\')
    project, layer = t[-4], t[-3]

    for i in files:
        file = project + '_' + layer + '_101_' + str(i)
        if not os.path.exists(os.path.join(path, file + '.gdi')) or not os.path.exists(os.path.join(path, file + '.def')):
            continue

        # 顺序读取图片
        figs = np.fromfile(os.path.join(path, file + '.gdi'), dtype='>u1')
        n = int(len(figs) / mc.WIDTH / mc.HEIGHT / 3)

        # 读取位置信息
        ft = open(os.path.join(path, file + '.def'), 'rb')
        a = ft.read()
        offset = a.find(b'EZAOI 1')
        offset += a[offset + 7] + 8
        ft.close()
        if int(np.fromfile(os.path.join(path, os.path.splitext(file)[0] + '.def'), dtype='int32', count=1, offset=offset)) != n:
            print('def\t', path)
            continue
        positions = np.fromfile(os.path.join(path, os.path.splitext(file)[0] + '.def'), dtype='int32', offset=offset+4)

        fig_t, position_t = [], []
        while len(figs) > 0:
            if positions[4] - positions[3] == 1350 and positions[6] - positions[5] == 1350:
                fig_t.append(np.array(figs[:mc.WIDTH * mc.HEIGHT * 3]).reshape(108, 108, 3)[:, :, [2, 1, 0]])
                position_t.append((positions[3]+675, positions[5]+675))
                positions = positions[19:]
                figs = figs[mc.WIDTH * mc.HEIGHT * 3:]
            else:
                positions = positions[11:]

        fig[i], position[i] = fig_t, position_t
    return fig, position


def tag_read(path):
    """
    读取工厂复检结果
    :param path: 复检结果所在文件夹路径
    :return: tags: 标签
    """
    t = path.split('\\')
    file = t[-1] + '_' + t[-2] + '.ini'  # 新VerifyResult文件路径
    # file = t[-2] + '_' + t[-1] + '.ini'  # 原VerifyResult文件路径
    if not os.path.exists(os.path.join(path, file)):
        return None

    tags, verifieds = {}, {}
    ver = open(os.path.join(path, file), 'r')
    ver_lines = ver.readlines()
    ver.close()

    i = 0
    while i < len(ver_lines):
        # if ver_lines[i][:10] == 'PanelCount':
            # ver_PanelCount = int(ver_lines[i][11:-1])
        if ver_lines[i][1:6] == 'Panel':
            panel = int(ver_lines[i][7:-2])
            # DefectCount = int(ver_lines[i + 1][12:-1])
            i += 2
            tag = {}
            if ver_lines[i + 1][:16] == 'VerifyCompeleted':
                if ver_lines[i + 1][17:21] == 'True':
                    verifieds[panel] = True
                else:
                    verifieds[panel] = False
                i += 3

            while ver_lines[i][0].isdigit():
                s = ver_lines[i].find('=')
                key = int(ver_lines[i][:s])
                value = int(ver_lines[i][s + 1:-1])
                tag[key] = value
                i += 3
            tags[panel] = tag

            if panel in verifieds.keys():
                continue
            if ver_lines[i + 1][:16] == 'VerifyCompeleted':
                if ver_lines[i + 1][17:21] == 'True':
                    verifieds[panel] = True
                else:
                    verifieds[panel] = False
                i += 3

        i += 1
    return tags, verifieds


if __name__ == '__main__':
    pass
