package com.example.demo.model.common;

import lombok.Data;

/**
 * @author : zhaoyingxiang
 * 校园板块新增task的入参DTO
 */
@Data
public class AddtaskXiaoyuanDTO {
    /**
     * 创建时间
     */
    private String c_time;

    /**
     * 价格
     */
    private String price;

    /**
     * 微信号
     */
    private String wechat;

    /**
     * 用户OpenID
     */
    private String openid;

    /**
     * 用户头像
     */
    private String avatar;

    /**
     * 校园分组
     */
    private String campusGroup;

    /**
     * 评论数量
     */
    private int commentNum;

    /**
     * 浏览数量
     */
    private int watchNum;

    /**
     * 点赞数量
     */
    private int likeNum;

    /**
     * radio分组
     */
    private String radioGroup;

    /**
     * 图片
     */
    private String img;

    /**
     * 地区
     */
    private String region;

    /**
     * 用户名称
     */
    private String userName;

    /**
     * 封面图片
     */
    private String cover;

    /**
     * 加密字段
     */
    private String encrypted;

	public String getC_time() {
		return c_time;
	}

	public void setC_time(String c_time) {
		this.c_time = c_time;
	}

	public String getPrice() {
		return price;
	}

	public void setPrice(String price) {
		this.price = price;
	}

	public String getWechat() {
		return wechat;
	}

	public void setWechat(String wechat) {
		this.wechat = wechat;
	}

	public String getOpenid() {
		return openid;
	}

	public void setOpenid(String openid) {
		this.openid = openid;
	}

	public String getAvatar() {
		return avatar;
	}

	public void setAvatar(String avatar) {
		this.avatar = avatar;
	}

	public String getCampusGroup() {
		return campusGroup;
	}

	public void setCampusGroup(String campusGroup) {
		this.campusGroup = campusGroup;
	}

	public int getCommentNum() {
		return commentNum;
	}

	public void setCommentNum(int commentNum) {
		this.commentNum = commentNum;
	}

	public int getWatchNum() {
		return watchNum;
	}

	public void setWatchNum(int watchNum) {
		this.watchNum = watchNum;
	}

	public int getLikeNum() {
		return likeNum;
	}

	public void setLikeNum(int likeNum) {
		this.likeNum = likeNum;
	}

	public String getRadioGroup() {
		return radioGroup;
	}

	public void setRadioGroup(String radioGroup) {
		this.radioGroup = radioGroup;
	}

	public String getImg() {
		return img;
	}

	public void setImg(String img) {
		this.img = img;
	}

	public String getRegion() {
		return region;
	}

	public void setRegion(String region) {
		this.region = region;
	}

	public String getUserName() {
		return userName;
	}

	public void setUserName(String userName) {
		this.userName = userName;
	}

	public String getCover() {
		return cover;
	}

	public void setCover(String cover) {
		this.cover = cover;
	}

	public String getEncrypted() {
		return encrypted;
	}

	public void setEncrypted(String encrypted) {
		this.encrypted = encrypted;
	}
    
    
}