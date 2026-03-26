import json
import random
import datetime
from typing import List, Dict, Any

class AcademicAIAssistant:
    """学术AI助手模拟类"""
    
    def __init__(self):
        """初始化模拟数据"""
        self.user_sessions = {}  # 用户会话记录
        self.literature_db = [
            {"id": 1, "title": "深度学习在自然语言处理中的应用", "authors": ["张伟", "李芳"], "keywords": ["深度学习", "NLP", "BERT"], "clicks": 0},
            {"id": 2, "title": "大语言模型的推理能力研究", "authors": ["王明", "赵静"], "keywords": ["大模型", "推理", "GPT"], "clicks": 0},
            {"id": 3, "title": "知识图谱与AI融合技术综述", "authors": ["刘强", "陈晨"], "keywords": ["知识图谱", "人工智能", "融合"], "clicks": 0},
            {"id": 4, "title": "多模态学习的进展与挑战", "authors": ["孙磊", "周婷"], "keywords": ["多模态", "视觉语言", "学习"], "clicks": 0},
            {"id": 5, "title": "AI在学术搜索中的优化策略", "authors": ["吴刚", "郑雪"], "keywords": ["学术搜索", "推荐算法", "优化"], "clicks": 0},
        ]
        
    def optimize_prompt(self, query: str) -> str:
        """优化提示词工程 - 模拟实际项目中的优化策略"""
        # 添加领域特定上下文
        enhanced_query = f"学术领域查询：{query}"
        
        # 根据查询长度调整提示策略
        if len(query) < 10:
            enhanced_query += "。请提供详细的相关文献。"
        else:
            enhanced_query += "。请推荐最相关的顶级文献。"
            
        return enhanced_query
    
    def search_literature(self, query: str, user_id: str = None) -> List[Dict[str, Any]]:
        """智能文献搜索与推荐 - 模拟大模型交互"""
        
        # 记录用户搜索行为
        if user_id:
            if user_id not in self.user_sessions:
                self.user_sessions[user_id] = {
                    "search_count": 0,
                    "click_count": 0,
                    "last_active": datetime.datetime.now().isoformat()
                }
            self.user_sessions[user_id]["search_count"] += 1
            self.user_sessions[user_id]["last_active"] = datetime.datetime.now().isoformat()
        
        # 应用优化后的提示词
        optimized_query = self.optimize_prompt(query)
        print(f"优化后的查询: {optimized_query}")
        
        # 模拟大模型处理 - 基于关键词匹配的简单推荐
        results = []
        query_lower = query.lower()
        
        for paper in self.literature_db:
            # 计算相关性分数（模拟排序策略优化）
            score = 0
            
            # 标题匹配
            if query_lower in paper["title"].lower():
                score += 3
                
            # 关键词匹配
            for keyword in paper["keywords"]:
                if query_lower in keyword.lower():
                    score += 2
                elif any(word in query_lower for word in keyword.lower().split()):
                    score += 1
            
            # 模拟点击率优化：给点击量低的文献适当加分（探索策略）
            if paper["clicks"] < 2:
                score += 1
                
            if score > 0:
                results.append({
                    **paper,
                    "relevance_score": score,
                    "recommendation_reason": f"与'{query}'相关，匹配关键词: {', '.join(paper['keywords'][:2])}"
                })
        
        # 按相关性排序（模拟排序策略）
        results.sort(key=lambda x: x["relevance_score"], reverse=True)
        
        # 限制返回数量，模拟实际推荐系统
        return results[:3]
    
    def record_click(self, paper_id: int, user_id: str = None) -> None:
        """记录用户点击行为 - 用于效果跟踪"""
        for paper in self.literature_db:
            if paper["id"] == paper_id:
                paper["clicks"] += 1
                print(f"文献 '{paper['title']}' 点击量更新为: {paper['clicks']}")
                
                # 更新用户会话数据
                if user_id and user_id in self.user_sessions:
                    self.user_sessions[user_id]["click_count"] += 1
                    
                    # 模拟效果跟踪：计算点击率提升
                    session = self.user_sessions[user_id]
                    if session["search_count"] > 0:
                        ctr = session["click_count"] / session["search_count"]
                        print(f"用户 {user_id} 当前点击率: {ctr:.2%}")
                break
    
    def get_user_metrics(self, user_id: str) -> Dict[str, Any]:
        """获取用户交互指标 - 模拟效果分析"""
        if user_id in self.user_sessions:
            session = self.user_sessions[user_id]
            return {
                "user_id": user_id,
                "搜索次数": session["search_count"],
                "点击次数": session["click_count"],
                "点击率": f"{session['click_count']/session['search_count']:.2%}" if session["search_count"] > 0 else "0%",
                "最后活跃时间": session["last_active"]
            }
        return {"error": "用户不存在"}
    
    def simulate_qa(self, question: str) -> str:
        """模拟问答功能 - 基于关键词的简单回答"""
        qa_mapping = {
            "深度学习": "深度学习通过多层神经网络学习数据表征，在NLP、CV等领域有广泛应用。",
            "大模型": "大语言模型通常指参数超过10亿的模型，具有强大的语言理解和生成能力。",
            "推荐算法": "推荐算法包括协同过滤、内容推荐等，学术推荐需考虑文献质量和相关性。",
            "优化策略": "优化策略包括提示词工程、排序算法改进、用户反馈闭环等。"
        }
        
        for keyword, answer in qa_mapping.items():
            if keyword in question:
                return f"问题: {question}\n回答: {answer}\n（基于知识库的模拟回答）"
        
        return f"问题: {question}\n回答: 这是一个关于'{question}'的学术问题。建议查阅相关文献获取详细信息。"

def main():
    """主函数 - 模拟学术AI助手工作流程"""
    print("=" * 50)
    print("学术AI助手模拟系统 v1.0")
    print("=" * 50)
    
    # 初始化助手
    assistant = AcademicAIAssistant()
    
    # 模拟用户会话
    user_id = "user_001"
    
    # 模拟搜索场景
    test_queries = ["深度学习", "大模型研究", "推荐算法优化"]
    
    for query in test_queries:
        print(f"\n[用户查询] {query}")
        print("-" * 30)
        
        # 搜索文献
        results = assistant.search_literature(query, user_id)
        
        if results:
            print(f"为您推荐以下 {len(results)} 篇相关文献：")
            for i, paper in enumerate(results, 1):
                print(f"{i}. {paper['title']}")
                print(f"   作者: {', '.join(paper['authors'])}")
                print(f"   推荐理由: {paper['recommendation_reason']}")
                print(f"   相关性分数: {paper['relevance_score']}")
                
                # 模拟用户点击（随机选择一篇）
                if random.random() > 0.5:
                    assistant.record_click(paper["id"], user_id)
        else:
            print("未找到相关文献")
        
        # 模拟问答功能
        if "优化" in query:
            answer = assistant.simulate_qa(query)
            print(f"\n[智能问答]\n{answer}")
    
    # 展示用户指标
    print("\n" + "=" * 50)
    print("用户交互指标分析（模拟效果跟踪）:")
    print("=" * 50)
    metrics = assistant.get_user_metrics(user_id)
    for key, value in metrics.items():
        print(f"{key}: {value}")
    
    # 模拟效果提升报告
    print("\n" + "=" * 50)
    print("优化效果模拟报告:")
    print("=" * 50)
    print("通过优化提示词工程与排序策略：")
    print("✓ 相关推荐点击率提升: 18% (模拟数据)")
    print("✓ 用户单次会话时长增加: 15% (模拟数据)")
    print("✓ 已完成三轮效果调优")
    
    # 展示文献点击统计
    print("\n文献点击量统计:")
    for paper in assistant.literature_db:
        print(f"  {paper['title'][:20]}...: {paper['clicks']} 次点击")

if __name__ == "__main__":
    main()