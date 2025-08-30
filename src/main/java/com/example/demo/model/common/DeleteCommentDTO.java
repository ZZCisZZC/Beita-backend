package com.example.demo.model.common;

import lombok.Data;

/**
 * @author : zhaoyingxiang
 * 删除评论请求DTO
 */
@Data
public class DeleteCommentDTO {
    /**
     * 用户OpenID
     */
    private String openid;

    /**
     * 关联的任务/帖子ID
     */
    private String pk;

	public String getOpenid() {
		return openid;
	}

	public void setOpenid(String openid) {
		this.openid = openid;
	}

	public String getPk() {
		return pk;
	}

	public void setPk(String pk) {
		this.pk = pk;
	}
    
    
}
