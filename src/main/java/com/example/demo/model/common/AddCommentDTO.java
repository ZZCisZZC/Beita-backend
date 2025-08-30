package com.example.demo.model.common;

import lombok.Data;

/**
 * @author : zhaoyingxiang
 * 添加评论请求DTO
 */
@Data
public class AddCommentDTO {
    /**
     * 用户OpenID
     */
    private String openid;
    
    /**
     * 回复目标
     */
    private String applyTo;
    
    /**
     * 用户头像
     */
    private String avatar;
    
    /**
     * 评论内容
     */
    private String comment;
    
    /**
     * 用户名称
     */
    private String userName;
    
    /**
     * 创建时间
     */
    private String c_time;
    
    /**
     * 关联的任务/帖子ID
     */
    private int pk;
    
    /**
     * 图片
     */
    private String img;
    
    /**
     * 评论层级
     */
    private String level;
    
    /**
     * 二级评论的parent id
     */
    private int pid;

	public String getOpenid() {
		return openid;
	}

	public void setOpenid(String openid) {
		this.openid = openid;
	}

	public String getApplyTo() {
		return applyTo;
	}

	public void setApplyTo(String applyTo) {
		this.applyTo = applyTo;
	}

	public String getAvatar() {
		return avatar;
	}

	public void setAvatar(String avatar) {
		this.avatar = avatar;
	}

	public String getComment() {
		return comment;
	}

	public void setComment(String comment) {
		this.comment = comment;
	}

	public String getUserName() {
		return userName;
	}

	public void setUserName(String userName) {
		this.userName = userName;
	}

	public String getC_time() {
		return c_time;
	}

	public void setC_time(String c_time) {
		this.c_time = c_time;
	}

	public int getPk() {
		return pk;
	}

	public void setPk(int pk) {
		this.pk = pk;
	}

	public String getImg() {
		return img;
	}

	public void setImg(String img) {
		this.img = img;
	}

	public String getLevel() {
		return level;
	}

	public void setLevel(String level) {
		this.level = level;
	}

	public int getPid() {
		return pid;
	}

	public void setPid(int pid) {
		this.pid = pid;
	}
    
    
}