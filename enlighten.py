#!/usr/bin/env python
#coding=utf-8

import cv2
import imageio
import numpy as np
import fastGuideFilter as fgf


def normValue(im):
    maxV = np.max(im)
    minV = np.min(im)
    im = (im-minV)/(maxV-minV+1e-6)
    return im


def calcNeiborGradient(im):
    knl = np.array([
        [0,0,0],
        [0,1,0],
        [0,0,0]
        ],dtype=np.float32)
    out = np.zeros(im.shape).astype(np.float32)
    for x,y in [[0,1],[1,0],[1,2],[2,1]]:
        knl[x,y] = -1.
        out += abs(cv2.filter2D(im,-1,knl))
        knl[x,y] = 0.
    return out


def KroneckerDelta(im,gim):
    buf = []
    for i in range(256):
        buf.append(np.sum(gim[im==i]))
    return buf


def HE(im,gim,K):
    out = np.zeros(im.shape)
    sumFi = np.sum(np.sum(gim))
    kd = KroneckerDelta(im,gim)
    P_a = kd/sumFi
    t = 0
    for i in range(K):
        t += P_a[i]
        out[np.where(im==i)] = (K-1)*t
    return out


def reflectGuideEnhance(src):
    eps = 1e-6
    r = 5
    epsi = 0.25
    gs = 2
    e = 0.6

    im = src.copy().astype(np.float32)
    Ain = np.max(src,2).astype(np.float32)/255.
    I = fgf.guideFilter(Ain,Ain,[r,r],epsi,gs)

    R = np.log10((Ain+eps)/(I+eps))
    gdR = calcNeiborGradient(R)
    B = HE(Ain*255.,gdR,256)
    Aout = B+e*R
    Aout = normValue(Aout)
    tmp = Aout/(Ain+eps)

    for i in range(3):
        im[:,:,i]*= tmp
    im = normValue(im)*255.

    return im
