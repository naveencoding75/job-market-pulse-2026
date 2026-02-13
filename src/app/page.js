"use client";

import { useState, useEffect } from "react";
import Papa from "papaparse";
import {
  BarChart,
  Bar,
  XAxis,
  YAxis,
  CartesianGrid,
  Tooltip,
  ResponsiveContainer,
  Cell
} from "recharts";
import { TrendingUp, Briefcase, Code, ShieldAlert } from "lucide-react";

// --- CONFIGURATION: The "WhiteList" of Skills ---
const TECH_STACK = [
  "python", "react", "node", "javascript", "typescript", "sql", "aws", "docker",
  "kubernetes", "java", "go", "rust", "linux", "security", "saas", "devops",
  "excel", "web3", "next.js", "tailwind"
];

export default function Home() {
  const [chartData, setChartData] = useState([]);
  const [totalJobs, setTotalJobs] = useState(0);
  const [topSkill, setTopSkill] = useState({ name: "", count: 0 });

  useEffect(() => {
    // 1. Fetch the CSV file from your public folder
    fetch("/remote_jobs_live.csv")
      .then((response) => response.text())
      .then((csvText) => {
        // 2. Parse CSV to JSON
        Papa.parse(csvText, {
          header: true,
          complete: (results) => {
            processJobData(results.data);
          },
        });
      });
  }, []);

  const processJobData = (rows) => {
    let skillCounts = {};
    let validJobCount = 0;

    rows.forEach((row) => {
      if (!row.Tags) return;
      
      validJobCount++;
      // Split tags "python, react" -> ["python", "react"]
      const tags = row.Tags.toLowerCase().split(",").map((t) => t.trim());

      tags.forEach((tag) => {
        // Normalize: 'node.js' -> 'node'
        let cleanTag = tag.includes("node") ? "node" : tag;

        if (TECH_STACK.includes(cleanTag)) {
          skillCounts[cleanTag] = (skillCounts[cleanTag] || 0) + 1;
        }
      });
    });

    // Sort and get Top 10
    const sortedSkills = Object.entries(skillCounts)
      .sort((a, b) => b[1] - a[1]) // Sort highest to lowest
      .slice(0, 10)
      .map(([name, count]) => ({ name: name.toUpperCase(), count }));

    setChartData(sortedSkills);
    setTotalJobs(validJobCount);
    setTopSkill(sortedSkills[0] || { name: "N/A", count: 0 });
  };

  return (
    <div className="min-h-screen bg-gray-950 text-white p-8 font-sans">
      {/* HEADER */}
      <header className="max-w-5xl mx-auto mb-12">
        <h1 className="text-4xl font-bold bg-gradient-to-r from-blue-400 to-purple-500 bg-clip-text text-transparent">
          The Job Market Pulse 2026
        </h1>
        <p className="text-gray-400 mt-2">
          Real-time analysis of {totalJobs} live remote job postings.
        </p>
      </header>

      {/* KPI CARDS */}
      <div className="max-w-5xl mx-auto grid grid-cols-1 md:grid-cols-3 gap-6 mb-12">
        <div className="bg-gray-900 p-6 rounded-xl border border-gray-800 shadow-lg">
          <div className="flex items-center gap-4 mb-2">
            <div className="p-3 bg-blue-900/30 rounded-lg text-blue-400">
              <Briefcase size={24} />
            </div>
            <h3 className="text-gray-400 text-sm uppercase tracking-wider">Total Jobs Analyzed</h3>
          </div>
          <p className="text-3xl font-bold">{totalJobs}</p>
        </div>

        <div className="bg-gray-900 p-6 rounded-xl border border-gray-800 shadow-lg">
          <div className="flex items-center gap-4 mb-2">
            <div className="p-3 bg-green-900/30 rounded-lg text-green-400">
              <TrendingUp size={24} />
            </div>
            <h3 className="text-gray-400 text-sm uppercase tracking-wider">#1 Trending Skill</h3>
          </div>
          <p className="text-3xl font-bold text-green-400">{topSkill.name}</p>
          <p className="text-sm text-gray-500 mt-1">Found in {topSkill.count} postings</p>
        </div>

        <div className="bg-gray-900 p-6 rounded-xl border border-gray-800 shadow-lg">
          <div className="flex items-center gap-4 mb-2">
            <div className="p-3 bg-purple-900/30 rounded-lg text-purple-400">
              <ShieldAlert size={24} />
            </div>
            <h3 className="text-gray-400 text-sm uppercase tracking-wider">Key Insight</h3>
          </div>
          <p className="text-lg font-medium text-gray-300">
            "Security" & "Go" are outperforming standard Frontend frameworks.
          </p>
        </div>
      </div>

      {/* MAIN CHART */}
      <div className="max-w-5xl mx-auto bg-gray-900 p-8 rounded-2xl border border-gray-800 shadow-2xl">
        <h2 className="text-2xl font-bold mb-6 flex items-center gap-2">
          <Code className="text-blue-500" /> Top 10 In-Demand Technologies
        </h2>
        
        <div className="h-[400px] w-full">
          <ResponsiveContainer width="100%" height="100%">
            <BarChart data={chartData} margin={{ top: 20, right: 30, left: 20, bottom: 5 }}>
              <CartesianGrid strokeDasharray="3 3" stroke="#374151" vertical={false} />
              <XAxis 
                dataKey="name" 
                stroke="#9CA3AF" 
                tick={{ fill: '#9CA3AF', fontSize: 12 }} 
                tickLine={false}
                interval={0}      
                angle={-20}       
                textAnchor="end"  
                height={60}       
              />
              <YAxis 
                stroke="#9CA3AF" 
                tick={{ fill: '#9CA3AF' }} 
                tickLine={false}
              />
              <Tooltip 
                contentStyle={{ backgroundColor: '#1F2937', borderColor: '#374151', color: '#fff' }}
                cursor={{ fill: '#374151', opacity: 0.4 }}
              />
              <Bar dataKey="count" radius={[4, 4, 0, 0]}>
                {chartData.map((entry, index) => (
                  <Cell key={`cell-${index}`} fill={index === 0 ? '#10B981' : '#6366F1'} />
                ))}
              </Bar>
            </BarChart>
          </ResponsiveContainer>
        </div>
        <p className="text-center text-gray-500 mt-6 text-sm">
          Source: Live API Data (RemoteOK) processed via Python & Next.js
        </p>
      </div>
    </div>
  );
}